user_type = GraphQLObjectType(
    name='User',
    fields={
        'id': GraphQLField(GraphQLString),
        'name': GraphQLField(GraphQLString)
    }
)

query_type = GraphQLObjectType(
    name='Query',
    fields={
        'users': GraphQLField(
            GraphQLList(user_type),
            resolver=lambda root, info: conn.cursor().execute('SELECT * FROM users').fetchall()
        )
    }
)

schema = GraphQLSchema(query=query_type)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
