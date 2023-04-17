@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    
@socketio.on('subscribe')
def handle_subscribe():
    conn.cursor().execute('LISTEN user_changed')


# CREATE OR REPLACE FUNCTION notify_user_changed()
# RETURNS trigger AS
# $$
# BEGIN
#     PERFORM pg_notify('user_changed', NEW.id::text);
#     RETURN NEW;
# END;
# $$ LANGUAGE plpgsql;

# CREATE TRIGGER user_changed_trigger
# AFTER INSERT OR UPDATE OR DELETE ON users
# FOR EACH ROW
# EXECUTE PROCEDURE notify_user_changed();


