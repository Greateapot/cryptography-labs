from __future__ import annotations
from itertools import batched
from pydantic import BaseModel

from cryptography.internal.utils.string_utils import bits_to_bytes, bytes_to_bits

INT_LENGHT = 4


class HaffmanAlgorithmNode(BaseModel):
    code: int | None = None  # byte
    count: int
    left: HaffmanAlgorithmNode | None = None
    right: HaffmanAlgorithmNode | None = None


def generate_nodes(data: bytes) -> list[HaffmanAlgorithmNode]:
    nodes: list[HaffmanAlgorithmNode] = list()
    for code in data:
        node: HaffmanAlgorithmNode | None = next(
            filter(lambda x: x.code == code, nodes),
            None,
        )

        if node is None:
            nodes.append(HaffmanAlgorithmNode(code=code, count=1))
        else:
            node.count += 1

    return nodes


def compress_tree_data(nodes: list[HaffmanAlgorithmNode]) -> bytes:
    tree_data = (len(nodes) * (INT_LENGHT + 1)).to_bytes(length=INT_LENGHT)
    for node in nodes:
        tree_data += node.code.to_bytes()
        tree_data += node.count.to_bytes(length=INT_LENGHT)
    return tree_data


def decompress_tree_data(tree_data: bytes) -> list[HaffmanAlgorithmNode]:
    nodes: list[HaffmanAlgorithmNode] = list()
    for code, *count in batched(tree_data, INT_LENGHT + 1):
        count = int.from_bytes(count)
        nodes.append(HaffmanAlgorithmNode(code=code, count=count))
    return nodes


def build_haffman_tree(nodes: list[HaffmanAlgorithmNode]) -> HaffmanAlgorithmNode:
    while len(nodes) > 1:
        nodes.sort(
            key=lambda x: (x.count, x.code if x.code is not None else -1),
            reverse=True,
        )
        node_i = nodes.pop()
        node_j = nodes.pop()

        left = node_i if node_j.count > node_i.count else node_j
        right = node_i if node_j is left else node_j

        nodes.append(
            HaffmanAlgorithmNode(
                count=node_i.count + node_j.count,
                left=left,
                right=right,
            )
        )

    return nodes[0]


def build_data_codes(tree: HaffmanAlgorithmNode) -> dict[int, str]:
    codes: dict[int, str] = dict()

    def _traverse(root: HaffmanAlgorithmNode, code: str) -> None:
        if root.left is not None:
            _traverse(root.left, code + "0")
        if root.right is not None:
            _traverse(root.right, code + "1")
        if root.code is not None:
            codes[root.code] = code

    _traverse(tree, "")

    return codes


def build_compressed_data(data: bytes, codes: dict[int, str]) -> bytes:
    bits = "".join([codes[d] for d in data])
    bit_length = len(bits)
    bit_off = bit_length % 8
    if bit_off:
        bits += "0" * (8 - bit_off)
    return int.to_bytes(bit_length, length=INT_LENGHT) + bytes(bits_to_bytes(bits))


def compress_haffman(data: bytes) -> bytes:
    nodes = generate_nodes(data)
    tree_data = compress_tree_data(nodes)
    tree = build_haffman_tree(nodes)
    codes = build_data_codes(tree)
    compressed_data = build_compressed_data(data, codes)
    return tree_data + compressed_data


def decompress_haffman(compressed_data: bytes) -> bytes:
    cdl = len(compressed_data)
    offset = 0

    assert cdl >= offset + INT_LENGHT
    tree_length = int.from_bytes(compressed_data[offset : offset + INT_LENGHT])
    offset += INT_LENGHT

    assert cdl >= offset + tree_length
    tree_data = compressed_data[offset : offset + tree_length]
    offset += tree_length

    assert cdl >= offset + INT_LENGHT
    bit_length = int.from_bytes(compressed_data[offset : offset + INT_LENGHT])
    bytes_length = (bit_length + 7) // 8
    offset += INT_LENGHT

    assert cdl >= offset + bytes_length
    bits = bytes_to_bits(compressed_data[offset : offset + bytes_length])
    del cdl, offset

    nodes = decompress_tree_data(tree_data)
    tree = build_haffman_tree(nodes)
    data = bytes()
    cursor: HaffmanAlgorithmNode = tree

    bit_count = 0
    while bit_count < bit_length:
        if bits[bit_count]:
            if cursor.right is not None:
                cursor = cursor.right
            else:
                data += cursor.code.to_bytes()
                cursor = tree.right
        else:
            if cursor.left is not None:
                cursor = cursor.left
            else:
                data += cursor.code.to_bytes()
                cursor = tree.left
        bit_count += 1

    if cursor.code is not None:  # append last
        data += cursor.code.to_bytes()

    return data


def compress_lzw(data: bytes):
    dictionary_size = 256
    dictionary = {i.to_bytes(): i for i in range(dictionary_size)}
    result = bytes()
    w = b""

    for c in data:
        wc = w + c.to_bytes()
        if wc in dictionary:
            w = wc
        else:
            result += dictionary[w].to_bytes(length=INT_LENGHT)
            dictionary[wc] = dictionary_size
            dictionary_size += 1
            w = c.to_bytes()

    if w:
        result += dictionary[w].to_bytes(length=INT_LENGHT)

    return result


def decompress_lzw(compressed: bytes):
    dictionary_size = 256
    dictionary = {i: i.to_bytes() for i in range(dictionary_size)}
    result = bytes()
    w = b""

    for k in [int.from_bytes(b) for b in batched(compressed, INT_LENGHT)]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dictionary_size:
            entry = w + w[0].to_bytes()
        else:
            raise ValueError(f"Bad compressed k: {k}")

        result += entry

        if w:
            dictionary[dictionary_size] = w + entry[0].to_bytes()
            dictionary_size += 1

        w = entry

    return result


def compress(data: bytes) -> bytes:
    haffman_compressed_data = compress_haffman(data)
    lzw_compressed_data = compress_lzw(haffman_compressed_data)
    return lzw_compressed_data


def decompress(lzw_compressed_data: bytes) -> bytes:
    haffman_compressed_data = decompress_lzw(lzw_compressed_data)
    decompressed_data = decompress_haffman(haffman_compressed_data)
    return decompressed_data


__all__ = (
    "compress",
    "decompress",
)
