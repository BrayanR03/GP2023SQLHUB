USE [BD_PythonBase]
GO
/****** Object:  User [rcero]    Script Date: 30/09/2023 18:01:53 ******/
CREATE USER [rcero] FOR LOGIN [rcero] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [rcero]
GO
/****** Object:  Table [dbo].[MARCA]    Script Date: 30/09/2023 18:01:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MARCA](
	[MarcaID] [int] IDENTITY(1,1) NOT NULL,
	[MarcaDescripcion] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_MARCA] PRIMARY KEY CLUSTERED 
(
	[MarcaID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PRODUCTO]    Script Date: 30/09/2023 18:01:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PRODUCTO](
	[ProductoID] [int] IDENTITY(1,1) NOT NULL,
	[ProductoDescripcion] [nvarchar](50) NOT NULL,
	[MarcaID] [int] NULL,
 CONSTRAINT [PK_PRODUCTO] PRIMARY KEY CLUSTERED 
(
	[ProductoID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  StoredProcedure [dbo].[BuscarProducto]    Script Date: 30/09/2023 18:01:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[BuscarProducto]
@NombreProducto nvarchar(50)
as
SELECT P.ProductoDescripcion AS PRODUCTO,M.MarcaDescripcion AS MARCA
FROM PRODUCTO P INNER JOIN MARCA M
ON M.MarcaID=P.MarcaID
WHERE P.ProductoDescripcion = NombreProducto
GO
