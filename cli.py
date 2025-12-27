import jsonManager
import click

@click.group
def cli():
    pass


@cli.command() #permite llamar funciones por termnal
@click.option('--description', required=True, help='description of the expense') #las opciones en terminal es --opcion
@click.option('--amount', required=True, help='amount of the expense')
@click.pass_context
def add(ctx, description, amount):
    if not description or not amount:
        ctx.fail('la descripcion y el monto son requeridos')
    else:
        expenses = jsonManager.read_json()
        new_id = len(expenses) + 1
        new_expense = {
            "id" : new_id,
            "description" : description,
            "amount" : amount
        }
        expenses.append(new_expense)
        jsonManager.write_Json(expenses)
        print(f"Descripcion {description} created succesfully with id {new_id}")

@cli.command()
@click.argument('id', type=int) #el argumneto en terminal seria delete 1
def delete(id):
    expenses = jsonManager.read_json()
    expense = next(x for x in expenses if x['id'] == id)
    if expense is None:
        print(f"Expense with id {id} not found")
    else:
        expenses.pop(id-1)
        jsonManager.write_Json(expenses)
        print(f"{expense['id']} - {expense['description']} - {expense['amount']} was deleted")

@cli.command()
def expenses():
    expenses = jsonManager.read_json()
    for x in expenses:
        print(f"{x['id']} - {x['description']} - {x['amount']}")

if __name__ == '__main__':
    cli()