import pyautogui


def fibonacci(n):
    """
    Calcula o n-ésimo número da sequência de Fibonacci.
    
    Args:
        n (int): Posição na sequência de Fibonacci
        
    Returns:
        int: O n-ésimo número de Fibonacci
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Exemplo de uso
if __name__ == "__main__":
    # Teste da função Fibonacci
    print("Sequência de Fibonacci:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")


