APP_NAME = MyAccountant

SRC_DIR = srcs
#TEST_DIR = tests

MAIN_SCRIPT = $(SRC_DIR)/main.py \

# Commande d'installation des dépendances
PIP_INSTALL = pip install -r requirements.txt

# Commande pour exécuter les tests
#TEST_CMD = pytest $(TEST_DIR)

.PHONY: all install test run clean

all: run

install:
	$(PIP_INSTALL)

# Cible pour exécuter les tests
# test:
# 	$(TEST_CMD)

run:
	python3 $(MAIN_SCRIPT)
# python3 $(MAIN_SCRIPT) example.pdf output.xlsx

clean:
	rm -rf __pycache__