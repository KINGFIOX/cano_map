import random


class MinHeap:
    """
    加强堆
    下标从0开始
    """

    def __init__(self) -> None:
        self._heap: list = []
        self._indexHeap: dict = {}
        self._heapSize = 0

    def __len__(self) -> int:
        return self._heapSize

    def __str__(self) -> str:
        return f"{self._heap}"

    def isEmpty(self) -> bool:
        return self._heapSize == 0

    def size(self) -> int:
        return self._heapSize

    def contains(self, obj) -> bool:
        return obj in self._indexHeap

    def peek(self):
        return self._heap[0]

    def push(self, item) -> None:
        self._heap.append(item)
        self._indexHeap[item] = self._heapSize
        self._heapify_up(self._heapSize - 1)
        self._heapSize += 1

    def pop(self) -> None:
        if len(self._heap) == 0:
            return None
        if len(self._heap) == 1:
            root = self._heap.pop()
            self._indexHeap.pop(root)
            self._heapSize -= 1
            return root

        self._swap(0, self._heapSize - 1)
        root = self._heap.pop()
        self._indexHeap.pop(root)
        self._heapSize -= 1
        self._heapify_down(0)
        return root

    def remove(self, obj) -> bool:
        # 删除obj
        index = self._indexHeap[obj]
        if index == None:
            return False
        else:
            replace_index = self._heapSize - 1
            replace_obj = self._heap[replace_index]
            self._swap(index, replace_index)
            self._heap.pop()
            self._indexHeap.pop(obj)
            self._heapSize -= 1
            replace_index = self._indexHeap[replace_obj]
            self._heapify_up(replace_index)
            self._heapify_down(replace_index)
            return True

    def resign(self, obj, re_val) -> bool:
        # obj是要修改的元素, re_val是修改后的元素
        index = self._indexHeap[obj]
        if index == None:
            return False
        self._heap[index] = re_val
        self._heapify_down(index)
        self._heapify_up(index)
        return True

    def _heapify_up(self, index: int) -> None:
        # 向上调整
        while index > 0:
            parent_index = (index - 1) // 2
            if self._heap[index] < self._heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index: int) -> None:
        # 向下调整
        left: int = index * 2 + 1
        while left < self._heapSize:
            # best是(最大的左右孩子)的(下标)
            best: int = (
                left + 1
                if left + 1 < len(self._heap)
                and self._heap[left + 1] < self._heap[left]
                else left
            )
            # best(左右孩子) 与 index(父节点) 比较
            best = best if self._heap[best] < self._heap[index] else index
            if best == index:
                break  # 最大节点是index, 就不用调整了
            self._swap(best, index)  # index与best交换
            index = best  # index向下
            left = index * 2 + 1

    def _swap(self, i: int, j: int) -> None:
        # 交换
        o1 = self._heap[i]
        o2 = self._heap[j]
        self._heap[j] = o1
        self._heap[i] = o2
        self._indexHeap[o1] = j
        self._indexHeap[o2] = i

    def getAllElements(self) -> list:
        # 获得树中的所有元素
        ans = []
        for c in self._heap:
            ans.append(c)
        return ans


if __name__ == "__main__":
    # 示例用法
    arr = [i for i in range(0, 20)]
    random.shuffle(arr)
    print(arr)
    min_heap = MinHeap()
    for i in arr:
        min_heap.push(i)
    print(min_heap)
    min_heap.remove(5)
    min_heap.remove(18)
    min_heap.resign(11, 25)
    arr = min_heap.getAllElements()
    print(arr)
    print(min_heap.contains(3))
    while not min_heap.isEmpty():
        print(f"{len(min_heap)}\t{min_heap.pop()}")
