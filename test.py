from cache import LRUCache

if __name__ == '__main__':
    c = LRUCache.new(5)

    c.insert(1, 10)
    c.insert(2, 20)
    c.insert(3, 30)
    c.insert(4, 40)
    c.insert(5, 50)
    print(c)

    c.get(1)
    print(c)

    c.get(4)
    print(c)

    c.insert(6, 60)
    print(c)