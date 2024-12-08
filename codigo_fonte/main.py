import os
from Assignment import assignPerTime

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    rooms_file = os.path.join(base_dir, "SIDS", "Rooms.txt")
    lessons_file = os.path.join(base_dir, "SIDS", "Lessons.txt")
    output_file = os.path.join(base_dir, "Output", "Lessons.txt")

    if not os.path.exists(rooms_file):
        print(f"Arquivo de salas não encontrado: {rooms_file}")
        return
    if not os.path.exists(lessons_file):
        print(f"Arquivo de aulas não encontrado: {lessons_file}")
        return

    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("Iniciando alocação de aulas...")
    try:
        assignPerTime(firstTime=True)
        print(f"Alocação concluída com sucesso. Resultado salvo em: {output_file}")
    except Exception as e:
        print(f"Ocorreu um erro durante a alocação: {e}")

if __name__ == "__main__":
    main()
