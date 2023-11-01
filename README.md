# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконала: Дишкант Христина Ігорівна (Група ІР-23)

### Лабораторна робота №1 (Варіант 3 Рівень 2)

Напишіть функцію для пошуку k-того найбільшого елемента в заданому масиві цілих чисел. Параметр k задається на вхід функції і визначає порядковий номер найбільшого елемента, який потрібно знайти. Наприклад, якщо k = 1, програма повинна знайти найбільший елемент в масиві. Якщо k = 2, програма повинна знайти другий за величиною елемент, і так далі.
​
Умови задачі:
​
- Масив цілих чисел передається у вашу функцію.
- Розмір масиву повинен бути не менше k.
- Програма повинна вивести k-тий найбільший елемент і його позицію (індекс) в масиві.
​
Приклад введення та виведення результату:
​
Вхідний масив: [15, 7, 22, 9, 36, 2, 42, 18] Задане k: 3 Знайдений 3-й найбільший елемент: 22 Позиція 3-го найбільшого елемента в масиві: 2
​
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` .
### Лабораторна робота №2 (Варіант 3 Рівень 2)

Горила Джекі  із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків (piles) з бананами, у і-тому кошику є певна кількість бананів Х. Кошики знаходяться під охороною, але охорона здійснює обхід зоопарку на Н годин, протягом якого Джекі може поласувати своєю улюбленою стравою.
​
Джекі може з'їсти за годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть К бананів звідти. Якщо кошик має менше, ніж К бананів, вона з'їдає всі банани з нього і більше не буде їсти бананів протягом цієї години.
Джекі любить їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш ніж охоронці повернуться.
​
Напишвть функцію, яка повертає мінімальне ціле число К, яке дозволить Джекі з'їсти всі банани на складі протягом Н годин, поки повернеться охорона.
​
Приклад 1:
piles = `[3,6,7,11]`, 
H = 8  
Результат: 
4  
​
Приклад 2:
piles = `[30,11,23,4,20]`,
H = 5  
Результат: 
30  

Приклад 3:
piles = `[30,11,23,4,20]`,
H = 6  
Результат: 
23
Важливо:
1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= `piles[i]` <= 10^9
​
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище.

### Лабораторна робота №3 (Варіант 3 Рівень 2)

Напишіть функцію, яка виконає операцію інвертування (перевернення) бінарного дерева таким чином, щоб лівий дочірній вузол став правим, а правий дочірній вузол став лівим.

Нехай у вас задане бінарне дерево такого вигляду:

    1
   / \
  2   3
 / \ / \
4  5 6  7

Ваша функція має повернути дерево, яке виглядатиме наступним чином:
    1
   / \
  3   2
 / \ / \
7  6 5  4

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

Ваша функція має мати такий вигляд:

```
def invert_binary_tree(tree) -> BinaryTree:
```
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу `BinaryTree` наступним чином:

```
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
```
Ваша функція має мати такий вигляд:

def invert_binary_tree(tree) -> BinaryTree:
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
Ваша функція має повернути об'єкт класу BinaryTree. Для спрощення тестування даної функції достатньо реалізувати порівняння значень вузлів дерева'''
