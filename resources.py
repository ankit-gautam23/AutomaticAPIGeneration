class User(Resource):
    def get(self, user_id):
        # Retrieve user from database and return as JSON
        return {'id': user_id, 'name': 'John Doe'}
    
    def post(self):
        # Insert new user into database and return as JSON
        return {'id': 1, 'name': 'John Doe'}
    
    def put(self, user_id):
        # Update user in database and return as JSON
        return {'id': user_id, 'name': 'John Doe'}
    
    def delete(self, user_id):
        # Delete user from database and return success message
        return {'message': 'User deleted successfully'}
    
api.add_resource(User, '/users', '/users/<int:user_id>')
