from .models import tbl_task, tbl_task_user_assoc
from user.models import tbl_user
from exceptions import ParameterError
from serializers import TaskSerializer
import datetime


def create_task(request):
    try:
        user_id = request.user.id
        user_obj = tbl_user.objects.get(id=user_id)
        task_serializer = TaskSerializer(data=request.data)
        if not task_serializer.is_valid():
            raise ParameterError('Invalid Parameters')
        
        task_obj = tbl_task(title = request.data.get('title'), description = request.data.get('description'), status = 'Pending', created_at = datetime.datetime.now(), updated_at = datetime.datetime.now(), task_type = request.data.get('task_type'))
        
        task_obj.save()
        
        
        task_user_assoc_obj = tbl_task_user_assoc(user_id = user_obj, task_id = task_obj)
        task_user_assoc_obj.save()
        
        return {'message': 'Task created successfully'}, 200
        
    except ParameterError as e:
        print(f"Error while creating task: {e}")
        return {'message': str(e)}, 400
    
    except Exception as e:
        print(f"Error while creating task: {e}")
        return {'message' : 'Internal Server Error'}, 400


def get_task(request, task_id = None):
    try:
        response = []
        user_id = request.user.id
        if not task_id:
            tasks = tbl_task.objects.filter(id__in = tbl_task_user_assoc.objects.filter(user_id=user_id).values_list('task_id', flat=True)).all()
        
        else:
            tasks = tbl_task.objects.filter(id = task_id).all()

        for task in tasks:
            response.append({
                'id'            : task.id,
                'user_id'       : user_id,
                'title'         : task.title,
                'description'   : task.description,
                'status'        : task.status,
                'task_type'     : task.task_type,
                'created_at'    : task.created_at,
                'updated_at'    : task.updated_at
            })
            
        return {'message' : 'Task fetched successfully', 'data' : response}, 200
        
    except ParameterError as e:
        print(f"Error while getting task: {e}")
        return {'message': str(e)}, 400
    
    except Exception as e:
        print(f"Error while getting task: {e}")
        return {'message' : 'Internal Server Error'}, 400

def update_task(request, task_id):
    try:
        user_id = request.user.id
        
        if not task_id:
            raise ParameterError('Invalid Parameters')
        

        task_obj = tbl_task.objects.filter(
            id=task_id,
            id__in=tbl_task_user_assoc.objects.filter(user_id=user_id).values_list('task_id')
        ).first()
        if not task_obj:
            raise ParameterError('Task not found')
        task_obj.title = request.data.get('title') if request.data.get('title') else task_obj.title
        task_obj.description = request.data.get('description') if request.data.get('description') else task_obj.description
        task_obj.status = request.data.get('status') if request.data.get('status') else task_obj.status
        task_obj.task_type = request.data.get('task_type') if request.data.get('task_type') else task_obj.task_type
        task_obj.updated_at = datetime.datetime.now()
        task_obj.save()

        return {'message': 'Task updated successfully'}, 200
    
    except ParameterError as e:
        print(f"Error while updating task: {e}")
        return {'message': str(e)}, 400
    
    except Exception as e:
        print(f"Error while updating task: {e}")
        return {'message' : 'Internal Server Error'}, 400

def delete_task(request, task_id):
    try:
        user_id = request.user.id
        if not task_id:
            raise ParameterError('Invalid Parameters')
        
        task_assoc_obj = tbl_task_user_assoc.objects.filter(user_id=user_id, task_id=task_id).first()
        task_obj = tbl_task.objects.get(id=task_id)
        
        if not task_obj or not task_assoc_obj:
            raise ParameterError('Task not found')
        
        task_assoc_obj.delete()
        task_obj.delete()
        
        return {'message': 'Task deleted successfully'}, 200
    
    except ParameterError as e:
        print(f"Error while updating task: {e}")
        return {'message': str(e)}, 400
    
    except Exception as e:
        print(f"Error while updating task: {e}")
        return {'message' : 'Internal Server Error'}, 400