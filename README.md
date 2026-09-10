# Enphase Dashboard 3.0

## La forma fácil de mantenerlo actualizado

1. Crea un repositorio en GitHub, por ejemplo `enphase-dashboard`.
2. Sube TODO el contenido de esta carpeta:
   - `index.html`
   - `Enphase_con_IA.xlsx`
   - carpeta `data`
   - carpeta `scripts`
   - carpeta `.github`
3. Activa GitHub Pages:
   **Settings → Pages → Deploy from a branch → main → /(root) → Save**
4. GitHub te dará una URL `https://TU-USUARIO.github.io/enphase-dashboard/`.
5. Cada vez que sustituyas `Enphase_con_IA.xlsx` por una versión nueva y hagas **Commit**, GitHub Actions ejecutará automáticamente `scripts/update_data.py`, actualizará `data/data.json` y el dashboard mostrará los nuevos datos.

### Importante
El Excel debe conservar la hoja `Datos` y las columnas utilizadas por el dashboard.

### Actualización sin tocar código
Solo tienes que:
- abrir el repositorio,
- reemplazar `Enphase_con_IA.xlsx`,
- guardar/commit.

No tienes que modificar `index.html`.

### Privacidad
GitHub Pages es público. No subas datos sensibles al repositorio. Si necesitas acceso privado, usa un hosting con autenticación o una solución con backend.
