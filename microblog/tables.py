from flask_table import Table, Col, LinkCol
 
class Results(Table):
    #id = Col('Id', show=False)
    song = Col('Song')
    artists = Col('Artists')
    #edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    #delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))