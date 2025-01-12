

class BitSeq:
    """A BitSeq is a sequence of bits

    Represented by a list of numbers that hold the packed bits,
    and a bunch of helper methods to help us build up a bit
    sequence and print/manipulate/observe the sequence of bits.
    """
    MAX_BITS_PER_INT = 16

    def __init__(self, max_bits_per_int=16):
        self.bits = []  # List of ints-- keep them 16-bit unsigned
        self.num_bits_in_seq = 0
        self.MAX_BITS_PER_INT = max_bits_per_int

    ## Only returns the first num_bits_in_seq characters
    ## e.g. get_bits_as_string() returns "1111"
    def get_bits_as_string(self):
        """Returns a string that represents the bits stored in this BitSeq.

        A space should be included after every MAX_BITS_PER_INT ints.
        If MAX_BIT_PER_INT = 4, a BitSeq would be returned as 1111 0000 0101 1001
        (with a break every 4 bits)
        """
        bit_str = ''.join(f"{bin(b)[2:].zfill(self.MAX_BITS_PER_INT)}" for b in self.bits)
        bit_str = bit_str[:self.num_bits_in_seq]
        return ' '.join([bit_str[i:i + self.MAX_BITS_PER_INT] for i in range(0, len(bit_str), self.MAX_BITS_PER_INT)])

    ## e.g. pack_bits("1111") will put the bits 1111 in the first available spot
    def pack_bits(self, new_bits_as_chars: str):
        """Given a string of 1s and 0s, packs relevant bits into this BitSeq"""
        ## For each bit/char in the input string:
        ##  determine if we need a new int in self.bits to hold more bits
        ##  Add a new bit to the last int
        for bit in new_bits_as_chars:
            if bit not in "01":  # 跳過非位元字符
                continue
            # 檢查是否需要新增一個整數來儲存位元
            if self.num_bits_in_seq % self.MAX_BITS_PER_INT == 0:
                self.bits.append(0)  # 修正 append 的用法
            # 如果當前位元是 '1'，更新位元在當前整數中的位置
            if bit == '1':
                self.bits[-1] |= 1 << (self.MAX_BITS_PER_INT - 1 - (self.num_bits_in_seq % self.MAX_BITS_PER_INT))
            self.num_bits_in_seq+=1
                

    def get_bit(self, which_bit: int) -> int:
        """Get the bit at position which_bit; 0-based index"""
        ## 0-based indexing
        ## If which_bit >= num_bits_in_seq throw an IndexError
        if which_bit >= self.num_bits_in_seq:
            raise IndexError("Bit index out of range")
        bit_pos = which_bit % self.MAX_BITS_PER_INT
        int_index = which_bit // self.MAX_BITS_PER_INT
        return (self.bits[int_index] >> (self.MAX_BITS_PER_INT - 1 - bit_pos)) & 1


class FreqTable:
    """A table that holds the frequency count of each character. """
    def __init__(self, input_str: str = ""):
        self.char_count = [0] * 256
        self.populate(input_str)

    def clear(self):
        """Resets the frequency counts such that all frequencies are 0"""
        self.char_count = [0] * 256

    def populate(self, input_str):
        """Given an input_str, update the frequency of each character in the table according to the string. """
        for c in input_str:
            self.char_count[ord(c)] += 1
        #pass

    def get_char_count(self, char):
        """Returns the current frequency count for the given char"""
        return self.char_count[ord(char)]

    def print_freq_table(self):
        """Print the frequency table in an easy to view format"""
        #pass
        print('Frequency:')
        for i,count in enumerate(self.char_count):
            if count > 0:
                print(f"'{chr(i)}' : {count}")


class HTree:
    """A HuffmanTree to be used to encode and decode messages. """
    def __init__(self, c=None, freq=0, p0=None, p1=None):
        self.char = c
        self.freq = freq
        self.p0 = p0
        self.p1 = p1

    def __lt__(self, other):
        # 如果頻率相同，按字母的 ASCII 值排序
        if self.freq == other.freq:
            return ord(self.char) < ord(other.char) if self.char and other.char else False
        return self.freq < other.freq
    
    def print_tree(self, level=0, path: str = ""):
        """Print the tree in an easy to understand format. """
        for i in range(level):
            print("--", end='')
        print(f"Char: {self.char}, count: {self.freq}. Path: {path}")
        if self.p0:
            self.p0.print_tree(level + 1, path + "0")
        if self.p1:
            self.p1.print_tree(level + 1, path + "1")

    ## For a specified tree and character,
    ##  determine if the character is in the tree,
    ##  and if so, the frequency count to get to it.
    ## Returns -1 if the character is not in the tree
    ## I used this as a helper; you can probably get away
    ##   without implementing it, but you'll have to update the
    ##   tests accordingly.
    def get_char_count(self, char):
        """Get the frequency count for a character in the tree. """
        if self.char == char:
            return self.freq
        # 若左子節點存在，遞歸查找左子樹
        if self.p0:
            left_count = self.p0.get_char_count(char)
            if left_count != -1:
                return left_count
        # 若右子節點存在，遞歸查找右子樹
        if self.p1:
            right_count = self.p1.get_char_count(char)
            if right_count != -1:
                return right_count
        # 若未找到字符，返回 -1
        return -1

    ## For a specified tree and character,
    ##  determine if the character is in the tree,
    ##  and if so, the path to get to it.
    ## Returns "" if the character is not in the tree
    ## I used this as a helper; you can probably get away
    ##   without implementing it, but you'll have to update the
    ##   tests accordingly.
    def get_char_path(self, target, path=""):
        """Get the path to a given character in this tree."""
        # 檢查當前節點是否是所尋找的字符
        if self.char == target:
            return path
        # 若左子節點存在，遞歸查找左子樹並在路徑中加入 '0'
        if self.p0:
            left_count = self.p0.get_char_path(target, path + "0")
            if left_count:
                return left_count
        # 若右子節點存在，遞歸查找右子樹並在路徑中加入 '1'
        if self.p1:
            right_count = self.p1.get_char_path(target, path + "1")
            if right_count:
                return right_count
        # 若未找到字符，返回空字串
        return ""

    ## Produces a serialized output of the tree, in the format:
    ## A0C1000D1001E1010F1011G1100H1101B111
    ## where it's [char][pathToChar][char][pathToChar]
    ## This is a LOW priority; this should be the last thing to implement
    def serialize(self, path: str = ""):
        """Write the tree into a string format to make it easy to save. """
        if self.char:
            return f"{self.char}{path}"
        left_serialized = self.p0.serialize(path + "0") if self.p0 else ""
        right_serialized = self.p1.serialize(path + "1") if self.p1 else ""
        return left_serialized + right_serialized

    ## Assumes all 1s and 0s are bits;
    ## A0C1000D1001E1010F1011G1100H1101B111
    ## Builds a tree based on the provided serialized tree string
    ## Doesn't populate it with frequencies, just the chars
    ## This isn't high priority, but can be helpful to easily
    ## create a new tree for testing
    def deserialize(self, tree_string):
        """Given a serialized tree string, make this tree represent it. """
        # 清空當前樹並根據字串重新建立
        self.char = None
        self.freq = 0
        self.p0 = None
        self.p1 = None
        i = 0
        # 讀取序列化字串，分別獲取字符和其路徑
        while i < len(tree_string):
            char = tree_string[i]
            path = ""
            i += 1
            while i <len(tree_string) and tree_string[i] in "01":
                path += tree_string[i]
                i += 1
            self.create_path(char,path)

    ## If the path exists, check if the char is the same and returns true/false
    ## If the path doesn't exist, creates the path and creates leaf node with the given char
    ## I used this as a helper for the deserialize process, but you may find
    ## it helpful.
    ## If you don't get around to implementing deserialize(), you probably don't need it.
    def create_path(self, char: str, path: str):
        """Populate a path to a node given the path. """
        current_node = self
        for step in path:
            if step == "0":
                if not current_node.p0:
                    current_node.p0 = HTree()
                current_node = current_node.p0
            elif step == "1":
                if not current_node.p1:
                    current_node.p1 = HTree()
                current_node = current_node.p1
        current_node.char = char


class LUT:
    """A LookUp Table to be used to store characters and their associated strings. """
    def __init__(self):
        self.representation = [""] * 256

    def print_lookup_table(self):
        """Print the table out in a nice to view manner"""
        print("Character Lookup Table:")
        for i,path in enumerate(self.representation):
            if path:
                print(f"'{chr(i)}' : {path}")
                

    ## Saves the path for a given char
    ## e.g. set_encoding('A', '10010')
    def set_encoding(self, char, path):
        """Save the encoding for a given character. """
        self.representation[ord(char)] = path

    ## Returns the path for a given char
    ## e.g. get_encoding('A') returns '10010'
    def get_encoding(self, char):
        """Return the encoding for a given character. """
        return self.representation[ord(char)]  # 根據字符的ASCII值索引編碼

    ## Given the root of a Huffman Tree, populate this lookup table.
    def populate_from_huffman_tree(self, htree_root: HTree):
        """Given a Huffman Tree, populate this LookupTable"""
        # 遞歸方式的協助函數，可以使用在 `populate_from_huffman_tree` 中。
        
        def traverse(node, path=""):
            if node.char:
                self.set_encoding(node.char, path)
                print(f"Encoding for '{node.char}': {path}")  # 輸出每個字符的編碼
            else:
                if node.p0:  # 若有左子節點，遞歸處理並加入 '0' 至路徑
                    traverse(node.p0, path+"0")
                if node.p1:  # 遞歸處理右子節點
                    traverse(node.p1,path+"1")
        traverse(htree_root)
        print("Final lookup table:", self.representation)  # 顯示整個編碼表

    ## I found it helpful to have a function such as this to help
    ## traverse the HTree to populate the table.
    ## Feel free to ignore it if you'd like, or write something for yourself.
    def create_lookup_table_helper(self, node, path, which_step):
        """Helper function to populate this LUT from a HuffmanTree. """
        if node.char:
            self.set_encoding(node.char,path)
        else:
            if node.p0:
                self.create_lookup_table_helper(node.p0,path+"0","left")
            if node.p1:
                self.create_lookup_table_helper(node.p1,path+"1","right")


class SecretMessage:
    """A class that holds an encoded message and the Huffman Tree that was used to create it. """
    def __init__(self, encoded_message: BitSeq, huffman_tree: HTree):
        self.encoded_bit_sequence = encoded_message
        self.huffman_tree = huffman_tree

import heapq  # 用於優先佇列實作
## This is the function that actually creates the HuffmanTree.
## Follow the process outlined in the README,
## in the "Creating the mapping: The Huffman Tree" section.
def create_encoding_tree(char_counts: FreqTable) -> HTree:
    """Create an encoding tree to be used to encode the message. """
    # 創建優先佇列（小頂堆），每個節點包含字符、頻率，並初始化為 Huffman 樹的葉子節點
    heap=[HTree(chr(i),freq) for i,freq in enumerate(char_counts.char_count) if freq>0]
    heapq.heapify(heap)
    # 當堆中還有多個節點時，不斷合併最小的兩個節點
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        # 創建新節點，其頻率為左右子節點頻率之和，並將兩個節點設為其子節點
        parent = HTree(None, left.freq+right.freq,left,right)
        # 將新節點加入堆中，維持頻率順序
        heapq.heappush(heap,parent)
    # 堆中剩下的唯一節點即為 Huffman 樹的根節點
    return heap[0] if heap else None

## The Encoder class is used to do encoding;
## It holds all the things we need to encode.
## This makes it helpful to inspect and test that
## all the pieces are working as expected.
class Encoder:
    """An Encoder encapsulates the entire process to create a SecretMessage via the use of a HuffmanTree. """
    def __init__(self):
        self.freq_table = None
        self.lookup_table = None
        self.huffman_tree = None
        self.encoded_bit_sequence = None

    ## Given a message,do all the steps to encode the message.
    ## When this is complete, the Encoder should have the
    ##  freq_table, lookup_table, huffman_tree, and encoded_bit_sequence
    ##  attributes should all be populated. (this allows us to test all the things)
    ## The huffman_tree and encoded_bit_sequence should be returned in a
    ##  SecretMessage object, so it can be "sent to a someone else".
    def encode(self, message_to_encode) -> SecretMessage:
        """Creates a SecretMessage from a raw message. """
        # 1. 建立頻率表
        self.freq_table = FreqTable(message_to_encode)
        
        # 2. 基於頻率表建立 Huffman 樹
        self.huffman_tree = create_encoding_tree(self.freq_table)
        print("Huffman Tree structure:")
        self.huffman_tree.print_tree()  # 顯示 Huffman 樹的結構
        
        # 3. 建立字符查找表
        self.lookup_table = LUT()
        self.lookup_table.populate_from_huffman_tree(self.huffman_tree)
        
        # 4. 使用查找表將訊息編碼為位元序列
        self.encoded_bit_sequence = BitSeq()
        for char in message_to_encode:
            encoded_char=self.lookup_table.get_encoding(char)# 獲取字符的 Huffman 編碼
            print(f"Encoding character '{char}' as '{encoded_char}'")  # Debug: 顯示每個字符的編碼過程
            self.encoded_bit_sequence.pack_bits(encoded_char)# 將編碼加入到位元序列中
        # 5. 返回 SecretMessage 物件，包含 Huffman 樹和編碼後的位元序列
        print("Encoded bit sequence:", self.encoded_bit_sequence.get_bits_as_string())
        return SecretMessage(self.encoded_bit_sequence,self.huffman_tree)

class Decoder:
    """A Decoder uses a Huffman Tree to decode a SecretMessage. """
    def __init__(self, huffman_tree: HTree):
        self.huffman_tree = huffman_tree

    ## Do the decoding of the provided message, using the
    ## self.huffman_tree.
    def decode(self, secret_message: BitSeq):
        """Decode the message, based on the HuffmanTree in this Decoder. """
        # 用於存放解碼結果的字符串列表
        decoded_message=[]
        # 透過 Huffman 樹遞歸解碼位元序列
        self.decode_helper(secret_message, self.huffman_tree, decoded_message, 0, [])
        
        return ''.join(decoded_message)

    ## This is a helper function to make decoding easier.
    ## I kept it in as a starter, but if you don't find it helpful,
    ## feel free to ignore it and take your own approach.
    ##
    ## Inputs:
    ## bit_seq: the BitSeq we're decoding
    ## cur_node: the current node in the HTree we're on
    ## out: a list of characters that have been emitted so far
    ## which_bit: which bit in the bit_seq we're at in our traversal
    ## path: the path that has gotten us to this point so far
    ##
    ## It's intended to be called recursively.
    ##
    ## Example first call:
    ## decode_helper(message, self.huffman_tree, [], 0, [])
    def decode_helper(self, bit_seq: BitSeq, cur_node, out: [], which_bit: int, path: []):
        # 檢查位元位置是否已到序列的末尾
        if which_bit >= bit_seq.num_bits_in_seq:
            return
        
        # 當前位元（0 或 1）
        bit = bit_seq.get_bit(which_bit)
        path.append(str(bit))  # 將位元加入路徑以跟蹤
        print(f"Decoding bit {bit} at position {which_bit}, current path: {''.join(path)}")  # 顯示當前處理的位元和路徑
        
        # 根據位元值選擇前進的子節點
        if bit == 0 and cur_node.p0:
            next_node=cur_node.p0
        elif bit == 1 and cur_node.p1:
            next_node=cur_node.p1
        else:
            return
        
        # 檢查是否到達葉子節點（字符節點）
        if next_node.char:
            out.append(next_node.char)  # 將字符加入解碼輸出
            print(f"Decoded character '{next_node.char}' from path {''.join(path)}")  # 顯示解碼的字符
            path.clear()
            self.decode_helper(bit_seq, self.huffman_tree, out, which_bit + 1, path)  # 回到根節點繼續解碼
        else:
            # 繼續前進至下一位元
            self.decode_helper(bit_seq, next_node, out, which_bit + 1, path)

