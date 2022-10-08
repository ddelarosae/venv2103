INSERT INTO Cliente (id, nombre, apellidos, telefono) 
VALUES ('104695', 'José', 'López Ariza', 3123675774);

INSERT INTO FormaDePago (id, nombre) VALUES (1, 'Tarjeta de crédito');
INSERT INTO FormaDePago (id, nombre) VALUES (2, 'Tarjeta débito');
INSERT INTO FormaDePago (id, nombre) VALUES (3, 'Efectivo');

INSERT INTO Producto (id, nombre, precio, existencia) VALUES ('99', 'Mouse', 25000, 64);
INSERT INTO Producto (id, nombre, precio, existencia) VALUES ('104', 'Teclado', '48000', 77);
INSERT INTO Producto (id, nombre, precio, existencia) VALUES ('47', 'Monitor', '368000', 23);

INSERT INTO Pedido (id, id_cliente, fecha, id_forma_pago) VALUES (1008, 109899, '06/12/20', 2);
INSERT INTO Pedido (id, id_cliente, fecha, id_forma_pago) VALUES (1009, 109899, '23/11/20', 3);
INSERT INTO Pedido (id, id_cliente, fecha, id_forma_pago) VALUES (1018, 104695, '01/12/20', 2);

INSERT INTO DetallePedido (sec, id_pedido, id_producto, precio, cantidad) VALUES (1, 1008, 104, 48000, 2);
INSERT INTO DetallePedido (sec, id_pedido, id_producto, precio, cantidad) VALUES (2, 1018, 104, 48000, 4);
INSERT INTO DetallePedido (sec, id_pedido, id_producto, precio, cantidad) VALUES (3, 1009, 47, 368000, 1);