import jsonManager
import click
from datetime import datetime
import calendar

@click.group
def cli():
    pass


@cli.command() #permite llamar funciones por termnal
@click.option('--description', required=True, help='description of the expense') #las opciones en terminal es --opcion
@click.option('--amount', required=True, help='amount of the expense', type=int)
@click.pass_context
def add(ctx, description, amount):
    if not description or not amount:
        ctx.fail('la descripcion y el monto son requeridos')
    else:
        fecha = datetime.now()
        fecha_formateada = fecha.strftime('%d/%m/%y')
        expenses = jsonManager.read_json()
        new_id = len(expenses) + 1
        new_expense = {
            "id" : new_id,
            "fecha" : fecha_formateada,
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
        print(f"{expense['id']} - {expense['fecha']} - {expense['description']} - {expense['amount']} was deleted")


@cli.command()
@click.option('--month', required=False, help='month of the expense', type=int)
def summary(month):
    expenses = jsonManager.read_json()
    total = 0
    if month:
        total = 0
        nombre_mes = calendar.month_name[month]
        registros = [r for r in expenses if int(r['fecha'].split('/')[1]) == month]
        total = sum(int(expense['amount']) for expense in registros)
        for expense in registros:
            total = total + int(expense['amount'])
        print(f"Total expenses for {nombre_mes}: {total}")
    else:
        for expense in expenses:
            total = total + int(expense['amount'])
        print(f"Total expenses: {total}")
    


@cli.command()
def list():
    expenses = jsonManager.read_json()
    for x in expenses:
        print(f"{x['id']} - {x['fecha']} - {x['description']} - {x['amount']}")



if __name__ == '__main__':
    cli()