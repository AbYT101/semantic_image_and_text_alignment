import axios from 'axios';
import { from, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { toast } from 'react-hot-toast';

export const composeImage = (files, description) => {
  const formData = new FormData();
  formData.append('logo', files.logo);
  formData.append('main_character', files.mainCharacter);
  formData.append('background', files.background);
  formData.append('cta', files.cta);
  formData.append('description', description);

  const response$ = from(
    axios.post('http://localhost:5000/compose', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      responseType: "blob",
    }).then(response => response)
  );

  return response$.pipe(
    catchError(error => {
      console.error('Error composing image:', error);
      toast.error('Error composing image!');
      return throwError(error);
    })
  );
};
