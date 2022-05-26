from Node import DoublyLinkedList

if __name__ == '__main__':

    new_linked_list = DoublyLinkedList()
    def options():
        opt = ''
        while (opt != 'x'):
            opt = str(input("Ingrese una de las siguientes opciones\n-----//-----//-----//-----//-----//-----//-----//-----\n1-) Listar elementos\n2-) Insertar al inicio\n3-) Insertar despues de\n4-) Insertar antes de\n5-) Insertar al final\n6-) Eliminar el primero\n7-) Eliminar el ultimo\n8-) Eliminar selección\n9-) Invertir Lista\nX-) Salir\t").lower())
            if opt == 'x':
                print('Bye')
            elif opt == '1':
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
            elif opt == '2':
                if (new_linked_list.start_node == None):
                    e = input('Inserte un primer valor: ')
                    new_linked_list.insert_in_emptylist(e)
                else:
                    new_linked_list.insert_at_start(e)
            elif opt == '3':
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
                x = input('Despues de que elemento desea insertar')
                e = input('Inserte un primer valor: ')
                new_linked_list.insert_after_item(x, e)
            elif opt == '4':
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
                x = input('Antes de que elemento desea insertar')
                e = input('Inserte un primer valor: ')
                new_linked_list.insert_before_item(x, e)
            elif opt == '5':
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
                e = input('Inserte un primer valor: ')
                new_linked_list.insert_at_end()
            elif opt == '6':
                new_linked_list.delete_at_start()
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
            elif opt == '7':
                new_linked_list.delete_at_end
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
            elif opt == '8':
                x = input('que elemento desea Eliminar')
                new_linked_list.delete_element_by_value(x)
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
            elif opt == '9':
                new_linked_list.delete_element_by_value(x)
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.reverse_linked_list()
            else:
                print('Opcion incorrecta')
    options()