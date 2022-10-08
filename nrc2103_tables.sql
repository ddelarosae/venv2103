CREATE TABLE FormaDePago(
	    id integer primary key,
	    nombre text
	);
CREATE TABLE Pedido(
    id integer primary key,
    fecha text,
    id_cliente integer references Cliente(id),
    id_forma_pago integer references FormaDePago(id)
);
CREATE TABLE Producto(
    id integer primary key,
    nombre text,
    precio real,
    existencia integer 
);
CREATE TABLE DetallePedido(
	    sec integer primary key,
	    cantidad integer,
	    precio real,
	    id_pedido integer references Pedido(id),
	    id_producto integer references Producto(id)
	);
