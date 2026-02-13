USE UniversidadDB;
GO

IF OBJECT_ID('Staging_Docentes', 'U') IS NOT NULL DROP TABLE Staging_Docentes;

CREATE TABLE Staging_Docentes(
	ID_Empleado INT,
	Nombre VARCHAR(255),
	Email VARCHAR(255),
	Facultad VARCHAR(100),
	Fecha_Contratacion VARCHAR(50),
	Sueldo_Base DECIMAL(18,2),
	Categoria VARCHAR(50)
);

IF OBJECT_ID('Staging_Presupuesto', 'U') IS NOT NULL DROP TABLE Staging_Presupuesto;

CREATE TABLE Staging_Presupuesto(
	ID_Transaccion UNIQUEIDENTIFIER,
	Departamento VARCHAR(100),
	Fecha VARCHAR(50),
	Tipo_Gasto VARCHAR(100),
	Monto DECIMAL(18,2),
	Aprobado VARCHAR(10)
);

GO