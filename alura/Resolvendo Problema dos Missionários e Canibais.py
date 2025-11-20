# Problema dos Missionários e Canibais
# Solução por busca em largura (BFS) para encontrar uma sequência válida de travessias.
# Estado: (M_esq, C_esq, barco), onde barco = 'E' (esquerda) ou 'D' (direita).
# Regras:
# - Barco leva 1 ou 2 pessoas por vez.
# - Em nenhuma margem os canibais podem superar o número de missionários,
#   exceto quando não há missionários naquela margem.
# - Movimento válido atualiza contagens de acordo com a posição do barco.

from collections import deque

def is_valid_state(m_left, c_left, m_right, c_right):
    # Valores devem estar nos limites [0,3]
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3 and 0 <= m_right <= 3 and 0 <= c_right <= 3):
        return False
    # Regra de segurança: canibais não podem superar missionários onde há missionários
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def neighbors(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    moves = []
    # Possíveis combinações que o barco pode levar
    candidates = [
        (1, 0),  # 1 missionário
        (2, 0),  # 2 missionários
        (0, 1),  # 1 canibal
        (0, 2),  # 2 canibais
        (1, 1),  # 1 missionário e 1 canibal
    ]

    if boat == 'E':
        # Levar pessoas da esquerda para a direita
        for dm, dc in candidates:
            new_m_left = m_left - dm
            new_c_left = c_left - dc
            new_m_right = m_right + dm
            new_c_right = c_right + dc
            if is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                moves.append(((new_m_left, new_c_left, 'D'), (dm, dc)))
    else:
        # Trazer pessoas da direita para a esquerda
        for dm, dc in candidates:
            new_m_left = m_left + dm
            new_c_left = c_left + dc
            new_m_right = m_right - dm
            new_c_right = c_right - dc
            if is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                moves.append(((new_m_left, new_c_left, 'E'), (dm, dc)))

    return moves

def bfs_solve():
    start = (3, 3, 'E')
    goal = (0, 0, 'D')  # Todos na direita e barco na direita
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path  # lista de (estado, movimento)
        for nxt, move in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [ (nxt, move) ]))
    return None

def print_solution(solution):
    if not solution:
        print("Nenhuma solução encontrada.")
        return

    print("Solução encontrada:\n")
    # Estado inicial
    print("Estado inicial: E: 3M,3C | D: 0M,0C | Barco: E")
    m_left, c_left, boat = 3, 3, 'E'

    step = 1
    for (state, move) in solution:
        dm, dc = move
        direction = "E → D" if boat == 'E' else "D → E"
        moved = []
        if dm: moved.append(f"{dm}M")
        if dc: moved.append(f"{dc}C")
        moved_str = " + ".join(moved)

        m_left, c_left, boat = state
        m_right = 3 - m_left
        c_right = 3 - c_left

        print(f"Passo {step}: {direction} levando {moved_str}")
        print(f"  E: {m_left}M,{c_left}C | D: {m_right}M,{c_right}C | Barco: {boat}")
        step += 1

    print("\nConcluído: todos os missionários e canibais estão na margem direita com segurança.")

if __name__ == "__main__":
    solution = bfs_solve()
    print_solution(solution)
