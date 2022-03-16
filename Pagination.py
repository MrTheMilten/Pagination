class Pagination:
    def __init__ (self,items=[],page_size=10):
        self.items=items
        self.page_size=page_size
        self.page_number=0
        self.book=[]
        for i in range(0,len(self.items),self.page_size):
            self.book.append(self.items[i:i+self.page_size])
    
    # возырвщвет элемент на этой странице
    def get_visible_items(self):
        return self.book[self.page_number]

    # предыдущая страница
    def prev_page (self):
        if self.page_number==1:
            return self
        else:
            self.page_number-=1
            return self

    # следующая страницаf
    def next_page(self):
        if self.page_number==len(self.book):
            return self
        else:
            self.page_number+=1
            return self

    # переход на первую тсраницу
    def first_page(self):
        self.page_number=0
        return self

    # переход на последнюю страницу
    def last_page(self):
        self.page_number=len(self.book)-1
        return self

    # переход на страницу
    def go_to_page(self,number):
        if number > len(self.book):
            self.page_number=len(self.book)-1
        elif number < 1:
            self.page_number=0
        else:
            self.page_number=number-1
        return self

    # возвращает номер текущей тсраницы
    def get_current_page(self):
        return self.page_number+1

    # возвращает размер страницы
    def get_page_size(self):
        return self.page_size

    # возвращает список строк
    def get_items(self):
        return self.items