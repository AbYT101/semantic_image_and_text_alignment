import axios from 'axios';
import { from, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { toast } from 'react-hot-toast';

export const composeImage = (files, description) => {
  const formData = new FormData();
  files.forEach(file => {
    formData.append(file.name, file);
  });
  formData.append('description', description);

  const response$ = from(
    axios.post('http://localhost:5000/compose', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }).then(response => response.data.image)
  );

  return response$.pipe(
    catchError(error => {
      console.error('Error composing image:', error);
      toast.error('Error composing image!');
      return throwError(error);
    })
  );
};
