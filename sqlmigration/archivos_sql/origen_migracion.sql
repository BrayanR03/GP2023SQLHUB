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
	[MarcaID] [int] NOT NULL,
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

INSERT [dbo].[MARCA] ([MarcaID], [MarcaDescripcion]) VALUES (1, N'GLORIA')
INSERT [dbo].[MARCA] ([MarcaID], [MarcaDescripcion]) VALUES (2, N'FRIOL')
INSERT [dbo].[MARCA] ([MarcaID], [MarcaDescripcion]) VALUES (3, N'PRIMOR')
INSERT [dbo].[MARCA] ([MarcaID], [MarcaDescripcion]) VALUES (4, N'CRISOL')
INSERT [dbo].[MARCA] ([MarcaID], [MarcaDescripcion]) VALUES (5, N'COMPASS')
INSERT [dbo].[MARCA] ([MarcaID], [MarcaDescripcion]) VALUES (6, N'DORINA')
INSERT [dbo].[MARCA] ([MarcaID], [MarcaDescripcion]) VALUES (7, N'LA DANESSA')
INSERT [dbo].[MARCA] ([MarcaID], [MarcaDescripcion]) VALUES (8, N'ANCHOR')

GO

INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (1, N'LECHE GLORIA 250ML', 1)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (2, N'FRIOL GALON', 2)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (3, N'FRIOL 3/4 LT', 2)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (4, N'FRIOL 1/2 lt', 2)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (5, N'FRIOL 5 LT', 2)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (6, N'FRIOL 10 LT', 2)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (7, N'PRIMOR 1LT', 3)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (8, N'PRIMOR 5 LT', 3)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (9, N'PRIMOR 3/4 LT', 3)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (10, N'CRISOL 1 LT', 4)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (11, N'CRISOL 1/2LT', 4)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (12, N'DORINA 225  x 1', 6)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (13, N'DORINA 225 x 12', 6)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (14, N'DANESSA 225 X12', 7)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (15, N'DANESSA 225 X 1', 7)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (16, N'ANCHOR 1KG', 8)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (17, N'ANCHOR  5 KG', 8)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (18, N'ANCHOR 1/2 KG', 8)
INSERT [dbo].[PRODUCTO] ([ProductoID], [ProductoDescripcion], [MarcaID]) VALUES (19, N'ANCHOR X 24', 8)