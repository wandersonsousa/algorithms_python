from string import ascii_uppercase as letters
from configuracao import Entrada  as input_from_file
import operator


def main():
    callback = banker_algorithm()
    print('\n \n')
    print('-- RESULTADO --')
    say_success('Sistema Seguro.') if not callback['deadlock'] else say_danger('Sistema não seguro.')

    print('Matriz de Recursos Disponíveis, após a execução: ')
    for resources_row in callback['available_resources']:
        print(resources_row)


def banker_algorithm():
    print('''
        [1] De forma manual 
        [2] Por arquivo de configuração
    ''')
    input_type = int(input('Como gostaria de passar os dados? '))

    # # data structures for algorithm
    
    resources = []
    allocated_processes = []
    available_resources = []
    needed_resourses = []

    if input_type == 1:
        input_data_from_terminal = get_algorithm_data_by_terminal()
        total_resources = input_data_from_terminal['total_resources']
        total_processes = input_data_from_terminal['total_processes']
        resources = input_data_from_terminal['resources']
        allocated_processes = input_data_from_terminal['allocated_processes']
        needed_resourses = input_data_from_terminal['needed_resourses']
        available_resources = input_data_from_terminal['available_resources']
    elif input_type == 2:
        total_resources = input_from_file.quantidade_de_recursos
        total_processes = input_from_file.quantidade_de_processos
        resources = input_from_file.quantidade_total_de_cada_recurso
        allocated_processes = input_from_file.matriz_de_recursos_ja_alocados
        needed_resourses = input_from_file.matriz_de_recursos_solicitados_por_cada_processo
        available_resources = set_available_resources(
        total_resources, resources, allocated_processes)

    
    # run algorithm logic
    return magic(total_processes, needed_resourses, available_resources, allocated_processes, resources)


def get_algorithm_data_by_terminal():
    total_resources = int(input('qntd de recursos: '))
    total_processes = int(input('qntd de processos: '))

    # get each resource quantity
    resources = get_each_resource_amount(total_resources)

    # get allocated resources qntt for each process
    allocated_processes = get_allocated_processes(
        total_processes, total_resources)

    # get needed resources for each process
    needed_resourses = get_needed_resources(total_processes, total_resources)

    # set available resources from data
    available_resources = set_available_resources(
        total_resources, resources, allocated_processes)
    
    return {
        'resources': resources,
        'allocated_processes': allocated_processes,
        'needed_resourses': needed_resourses,
        'available_resources': available_resources,
        'total_processes': total_processes,
        'total_resources': total_resources
    }


def magic(total_processes, needed_resourses, available_resources, allocated_processes, resources):
    executed_processes = []
    deadlock = False
    msg_callback = {
        'deadlock': bool,
        'available_resources': list
    }
    while len(executed_processes) < total_processes:
        for process_index in range(len(needed_resourses)):
            if process_index in executed_processes:
                # process already executed
                continue
            rq_process, av_resource, current_allocate_process = needed_resourses[
                process_index], available_resources[-1], allocated_processes[process_index]

            if check_if_it_can_run(rq_process, av_resource):
                # run process request
                available_resources.append(
                    list(map(operator.add, current_allocate_process, av_resource)))
                allocated_processes[process_index] = fill_list_with(
                    current_allocate_process, 0)
                executed_processes.append(process_index)
                continue
            else:
                # process cannot be runned
                if resources == available_resources[-1]:
                    deadlock = True
                    msg_callback['deadlock'] = deadlock
                    msg_callback['available_resources'] = available_resources
                    return msg_callback
                continue
    msg_callback['deadlock'] = deadlock
    msg_callback['available_resources'] = available_resources
    return msg_callback


def set_available_resources(total_resources, resources, allocated_processes):
    available_resources = []
    allocated_resources = []
    for i in range(total_resources):
        for j in range(len(allocated_processes)):
            al_process = allocated_processes[j]
            if j == 0:
                allocated_resources.append(al_process[i])
            else:
                allocated_resources[i] += al_process[i]
    available_resource_row = []
    for i in range(total_resources):
        al_resource = allocated_resources[i]
        total_resource_value = resources[i]
        available_resource_row.append(total_resource_value - al_resource)
    available_resources.append(available_resource_row)
    return available_resources


def get_each_resource_amount(total_resources):
    resources = []
    for i in range(total_resources):
        resource_quantity = int(
            input('qntd do recurso {}: '.format(letters[i])))
        resources.append(resource_quantity)
    return resources


def get_allocated_processes(total_processes, total_resources):
    allocated_processes = []
    for i in range(total_processes):
        process = []
        for j in range(total_resources):
            process.append(int(input(
                'Valor de alocação de recurso {} para processo {}: '.format(letters[j], letters[i]))))

        allocated_processes.append(process)
    return allocated_processes


def get_needed_resources(total_processes, total_resources):
    needed_resourses = []
    for i in range(total_processes):
        needed_resourse = []
        for j in range(total_resources):
            needed_resourse.append(int(input(
                'Valor requisitado de recurso {} para processo {}: '.format(letters[j], letters[i]))))
        needed_resourses.append(needed_resourse)
    return needed_resourses


def fill_list_with(array, el):
    for n in range(len(array)):
        array[n] = el
    return array


def check_if_it_can_run(needed_resources, available_resources):
    for i in range(len(available_resources)):
        if available_resources[i] < needed_resources[i]:
            return False
    return True

def say_success(out_text):
    print('\033[1;32;40m {} \033[0m'.format(out_text))
def say_danger(out_text):
    print('\033[1;31;40m {} \033[0m'.format(out_text))
    
if __name__ == '__main__':
    main()
