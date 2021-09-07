from person_node import PersonNode
class PersonTree():
    def has_priority(self, a, b):
        if a.calculate_weight() > b.calculate_weight():
            return True
        elif a.calculate_weight() == b.calculate_weight():
            people = [a.name, b.name]
            people.sort()
            if a.name == people[0]:
                return True
            else:
                return False
        else:
            return False
 
    def insert(self, root, person):
     
        if root == None:
            return PersonNode(person)
        elif not self.has_priority(person, root.person):
            root.left = self.insert(root.left, person)
        else:
            root.right = self.insert(root.right, person)
 
        root.height = max(self.calculate_height(root.left), self.calculate_height(root.right)) + 1
 
        balance = self.calculate_balance(root)
 
        if balance > 1 and not self.has_priority(person, root.left.person):
            return self.rotate_right(root)
        elif balance > 1 and self.has_priority(person, root.left.person):
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
 
        if balance < -1 and self.has_priority(person, root.right.person):
            return self.rotate_left(root)
        elif balance < -1 and not self.has_priority(person, root.right.person):
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
 
        return root
 
    def rotate_left(self, target):
        next = target.right
        subtree = next.left
        next.left = target
        target.right = subtree
 
        target.height = max(self.calculate_height(target.left), self.calculate_height(target.right)) + 1
        next.height = max(self.calculate_height(next.left), self.calculate_height(next.right)) + 1
 
        return next
 
    def rotate_right(self, target):
        next = target.left
        subtree = next.right
 
        next.right = target
        target.left = subtree
        target.height = max(self.calculate_height(target.left), self.calculate_height(target.right)) + 1
        next.height = max(self.calculate_height(next.left), self.calculate_height(target.right)) + 1
 
        return next
 
    def calculate_height(self, root):
        if root == None:
            return 0
 
        return root.height
 
    def calculate_balance(self, root):
        if root == None:
            return 0
 
        return self.calculate_height(root.left) - self.calculate_height(root.right)

    def minimum_node(self, root):
        if root == None or root.left == None:
            return root
 
        return self.minimum_node(root.left)
 
    def preOrder(self, root):
 
        if root == None:
            return
 
        print("{0} ".format(root.person.name), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def remove(self, root, person):
 
        if root == None:
            return root
 
        elif not self.has_priority(person, root.person):
            print(1)
            root.left = self.remove(root.left, person)
        elif self.has_priority(person, root.person):
            print(2)
            root.right = self.remove(root.right, person)
        else:
            if root.left == None:
                print(3)
                new_root = root.right
                root = None
                return new_root
            elif root.right == None:
                print(4)
                new_root = root.left
                root = None
                return new_root
 
            new_root = self.minimum_node(root.right)
            root.person = new_root.person
            root.right = self.remove(root.right, new_root.val)
 
        if root == None:
            return root
 
        root.height = max(self.calculate_height(root.left), self.calculate_height(root.right)) + 1
 
        balance = self.calculate_balance(root)
 
        if balance > 1 and self.calculate_balance(root.left) >= 0:
            return self.rightRotate(root)
        elif balance > 1 and self.calculate_balance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and self.calculate_balance(root.right) <= 0:
            return self.leftRotate(root)
        elif balance < -1 and self.calculate_balance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)     
 
        return root
