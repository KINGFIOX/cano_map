import random


class HeapGreater:
    """
    小根堆
    堆的下标是从0到heapsize-1, 和王道的堆不一样
    因此, 左孩子是left = index * 2 - 1, 右孩子是rigt =  index * 2
    """

    def __init__(self) -> None:
        # 变量列表
        self._heap: list = []  # 实际的堆结构
        self._indexMap: dict = {}  # hash表, obj : index(对象索引下标)
        self._heapSize: int = 0  # 堆的大小

    def __len__(self):
        return self._heapSize

    def isEmpty(self) -> bool:
        return self._heapSize == 0

    def size(self) -> int:
        return self._heapSize

    def contains(self, obj) -> bool:
        return obj in self._indexMap

    def peek(self):
        return self._heap[0]

    def push(self, obj) -> None:
        self._heap.append(obj)
        self._indexMap[obj] = self._heapSize
        self._heapInsert(self._heapSize)
        self._heapSize += 1

    def pop(self):
        # ans是obj
        ans = self._heap[0]
        self._swap(0, self._heapSize - 1)
        del self._indexMap[ans]
        self._heapSize -= 1
        del self._heap[self._heapSize]
        self._heapify(0)
        return ans

    def remove(self, obj) -> None:
        # 获得heap的最后一个元素, replace是objection
        replace = self._heap[self._heapSize - 1]
        index: int = self._indexMap[obj]
        del self._indexMap[obj]
        self._heapSize -= 1
        del self._heap[self._heapSize]
        if not obj == replace:
            self._heap[index] = replace
            self._indexMap[replace] = index
            self.resign(replace)

    def getAllElements(self) -> list:
        # 获得树中的所有元素
        ans = []
        for c in self._heap:
            ans.append(c)
        return ans

    def resign(self, obj) -> None:
        # val:obj, 向上调整, 向下调整
        self._heapInsert(self._indexMap[obj])
        self._heapify(self._indexMap[obj])

    def _heapInsert(self, index: int):
        # 向上调整
        while self._heap[index] < self._heap[(index - 1) // 2]:
            self._swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def _heapify(self, index: int) -> None:
        # 向下调整
        left: int = index * 2 + 1
        while left < self._heapSize:
            # best是(最大的左右孩子)的(下标)
            best: int = (
                left + 1
                if left + 1 < self._heapSize and self._heap[left + 1] < self._heap[left]
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
        # 树中i,j交换, 记录obj, 并保存obj的下标, 即(obj, index)
        o1 = self._heap[i]
        o2 = self._heap[j]
        self._heap[i] = o2
        self._heap[j] = o1
        self._indexMap[o2] = i
        self._indexMap[o1] = j


if __name__ == "__main__":
    arr = [my_int(i) for i in range(0, 20)]
    random.shuffle(arr)
    gth = HeapGreater()
    for i in arr:
        gth.push(i)
    while not gth.isEmpty():
        print(gth.pop().value)

    print("hello world")
