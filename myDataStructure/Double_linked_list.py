class Node(object):
    # 双向链表节点
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    # 双向链表
    def __init__(self):
        self._head = None

    def is_empty(self):
        # 判断链表是否为空
        return self._head == None

    def get_length(self):
        # 返回链表的长度
        cur = self._head
        count = 0
        while cur != None:
            count = count+1
            cur = cur.next
        return count

    def print_list(self):
        # 遍历链表
        items_list = []
        cur = self._head
        while cur != None:
            items_list.append(cur.item)
            # print(cur.item)
            cur = cur.next

        print(items_list)
        # print("")

    def add(self, item):
        # 头部插入元素
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将 node 赋值给 _head
            self._head = node
        else:
            # 将 node 的 next 属性指向头节点 _head
            node.next = self._head
            # 将头节点 _head 的 prev 属性指向 node
            self._head.prev = node
            # 将 node 赋值给 _head
            self._head = node

    def append(self, item):
        # 尾部插入元素
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将 node 赋值给 _head
            self._head = node
        else:
            # 循环移动到链表尾部结点的位置
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾结点 cur 的 next 属性指向 node
            cur.next = node
            # 将 node 的 prev 属性指向 cur
            node.prev = cur

    def search(self, item):
        # 查找元素是否存在
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        # 在指定位置添加节点
        if pos <= 0:
            self.add(item)
        elif pos > (self.get_length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 将 node 的 prev 属性指向 cur
            node.prev = cur
            # 将 node 的 next 属性指向 cur 的下一个节点
            node.next = cur.next
            # 将 cur 的下一个节点的 prev 属性指向 node
            cur.next.prev = node
            # 将 cur 的 next 指向 node
            cur.next = node

    def remove(self, item):
        # 删除元素
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的 prev 属性设置为 None
                    cur.next.prev = None
                    # 将 _head 指向第二个节点
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    # 将 cur 的前一个节点的 next 指向 cur 的后一个节点
                    cur.prev.next = cur.next
                    # 将 cur 的后一个节点的 prev 指向 cur 的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

    def reverse(self):
        """
        将链表头尾反转
        :return:
        """
        prev = None
        current = self._head # 将头节点保存在current中

        # 当链表为非空的时候，需要执行相应反转的操作
        # 分别将相邻的两个节点的前驱后继关系进行反转
        while current:
            next_node = current.next    # 将下一个节点保存在next_node中
            current.next = prev     # 由于反转链表，因此头节点反转后，成为尾节点，应该指向None
            current.prev = next_node    # 尾节点的前驱应指向原本的后继

            prev = current      # 更新prev，向后移动
            current = next_node # 更新current，向后移动

        # 到达链表尾部时，需要特殊处理
        self._head = prev

    def init_list(self, list):
        for item in list:
            self.append(item)