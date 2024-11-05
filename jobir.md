Шаг 1: Загрузка необходимые библиотеки и данные
для установлены библиотеки scikit-learn и pandas. Набор данных о диабете доступен в scikit-learn.

Шаг 2: Разделение данные на обучающую и тестовую выборки


from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import pandas as pd

# Загрузка данных о диабете
data = load_diabetes(as_frame=True)
df = data.frame

# Искусственно создадим целевой признак как бинарный (например, диабет/нет диабета) для задачи классификации
# Разделим данные на два класса на основе среднего значения целевого признака
df['target_class'] = (df['target'] > df['target'].mean()).astype(int)

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    df.drop(columns=['target', 'target_class']),
    df['target_class'],
    test_size=0.3,
    random_state=42
)
Шаг 3: Проверка сбалансированности классов
Чтобы убедиться, что распределение классов одинаково, рассчитаем количество элементов каждого класса в обучающей и тестовой выборках.

# Подсчёт классов в обучающей выборке
train_class_distribution = y_train.value_counts(normalize=True)

# Подсчёт классов в тестовой выборке
test_class_distribution = y_test.value_counts(normalize=True)

# Вывод результатов
print("Распределение классов в обучающей выборке:")
print(train_class_distribution)

print("\nРаспределение классов в тестовой выборке:")
print(test_class_distribution)

Шаг 4: Анализ результатов
Если распределение классов в обучающей и тестовой выборках совпадает или близко, можно считать, что выборки сбалансированы.
В случае значительных отличий, можно попробовать изменить параметр random_state в train_test_split или использовать методы для балансировки, такие как StratifiedKFold.