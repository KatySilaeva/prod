--
-- ���� ������������ � ������� SQLiteStudio v3.4.4 � �� ��� 11 16:22:45 2023
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: food
CREATE TABLE IF NOT EXISTS food (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, dish TEXT NOT NULL, type TEXT NOT NULL, price INTEGER NOT NULL);
INSERT INTO food (id, dish, type, price) VALUES (1, '����������', '�����', 100);
INSERT INTO food (id, dish, type, price) VALUES (2, '�����', '������', 60);
INSERT INTO food (id, dish, type, price) VALUES (3, '��������', '������', 60);
INSERT INTO food (id, dish, type, price) VALUES (4, '�����', '������', 100);
INSERT INTO food (id, dish, type, price) VALUES (5, '�������', '����', 140);
INSERT INTO food (id, dish, type, price) VALUES (6, '������', '����', 85);
INSERT INTO food (id, dish, type, price) VALUES (7, '���', '����', 17);
INSERT INTO food (id, dish, type, price) VALUES (8, '�������', '����', 9);
INSERT INTO food (id, dish, type, price) VALUES (9, '���������', '����', 34);
INSERT INTO food (id, dish, type, price) VALUES (10, '�������', '����', 30);
INSERT INTO food (id, dish, type, price) VALUES (11, '������', '�������� ���������', 75);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
