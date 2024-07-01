-- Selecciona todos los campos de la tabla 'repuesto'

SELECT r.*
-- Desde la tabla 'repuesto' referenciada como 'r'

FROM repuesto r

-- Une la tabla 'actualizacion' referenciada como 'a' donde el ID de última actualización de 'repuesto' coincide con el ID de 
'actualizacion'

JOIN actualizacion a ON r.ultima_actualizacion_id = a.id

-- Une la tabla 'proveedor' referenciada como 'p' donde el ID del proveedor en 'actualizacion' coincide con el ID en 'proveedor'

JOIN proveedor p ON a.proveedor_id = p.id

-- Filtra los resultados para incluir solo aquellos donde el nombre del proveedor es 'AutoFix'

WHERE p.nombre = 'AutoFix'

-- Y la fecha de la actualización es dentro del último mes

AND a.fecha > DATE_SUB(NOW(), INTERVAL 1 MONTH);


-- Actualiza la tabla 'repuesto'

UPDATE repuesto

-- Incrementa el precio de los repuestos en un 15%
SET precio = precio * 1.15
-- Filtra los repuestos cuyas marcas correspondan a los nombres dados

WHERE marca_id IN (
    -- Subconsulta para obtener los IDs de las marcas especificadas
    SELECT id FROM marca
    WHERE nombre IN ('ELEXA', 'BERU', 'SH', 'MASTERFILT', 'RN')
);


-- Selecciona el nombre de la marca y el promedio de precios de los repuestos asociados a cada marca

SELECT m.nombre AS Marca, AVG(r.precio) AS Promedio_Precio

-- Desde la tabla 'marca' referenciada como 'm'

FROM marca m

-- Une la tabla 'repuesto' referenciada como 'r' donde los IDs de marca coinciden

JOIN repuesto r ON m.id = r.marca_id

-- Agrupa los resultados por marca para calcular el promedio por grupo

GROUP BY m.nombre;


-- Selecciona todos los campos de los repuestos que no tienen descripción asignada

SELECT *

-- Desde la tabla 'repuesto'

FROM repuesto

-- Filtra los repuestos donde la descripción es NULL o vacía

WHERE descripcion IS NULL OR descripcion = '';


-- Selecciona el nombre del proveedor y cuenta el número total de repuestos asociados a cada proveedor

SELECT p.nombre, COUNT(r.id) AS num_repuestos

-- Desde la tabla de proveedores

FROM proveedor p

-- Une la tabla de proveedores con la tabla de repuestos utilizando el ID del proveedor

JOIN repuesto r ON p.id = r.proveedor_id

-- Agrupa los resultados por el ID y el nombre del proveedor para poder contar los repuestos de cada uno

GROUP BY p.id, p.nombre

-- Filtra los grupos para incluir solo aquellos con al menos 1000 repuestos

HAVING COUNT(r.id) >= 1000;


-- Selección del repuesto más caro de cada proveedor

SELECT r.proveedor_id, MAX(r.precio) AS precio_maximo
FROM repuesto r
GROUP BY r.proveedor_id;

-- Actualización de precios con recargo del 30%

UPDATE repuesto

-- Aplica el aumento del 30% al precio actual

SET precio = precio * 1.30  

-- Identifica los proveedores específicos

WHERE proveedor_id IN (
    SELECT id FROM proveedor
    WHERE nombre IN ('AutoRepuestos Express', 'Automax')  
)
AND precio > 50000 AND precio < 100000;  -- Condición del rango de precios
