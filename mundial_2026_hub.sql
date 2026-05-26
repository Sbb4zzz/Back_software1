-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-05-2026 a las 04:06:19
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mundial_2026_hub`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coleccion_usuario`
--

CREATE TABLE `coleccion_usuario` (
  `usuario_id` varchar(36) NOT NULL,
  `lamina_id` int(11) NOT NULL,
  `cantidad` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `coleccion_usuario`
--

INSERT INTO `coleccion_usuario` (`usuario_id`, `lamina_id`, `cantidad`) VALUES
('550e8400-e29b-41d4-a716-446655440000', 23, 1),
('550e8400-e29b-41d4-a716-446655440000', 27, 1),
('550e8400-e29b-41d4-a716-446655440000', 48, 1),
('550e8400-e29b-41d4-a716-446655440000', 51, 1),
('550e8400-e29b-41d4-a716-446655440000', 54, 1),
('550e8400-e29b-41d4-a716-446655440000', 58, 2),
('550e8400-e29b-41d4-a716-446655440000', 61, 1),
('550e8400-e29b-41d4-a716-446655440000', 62, 1),
('550e8400-e29b-41d4-a716-446655440000', 68, 1),
('550e8400-e29b-41d4-a716-446655440000', 69, 1),
('550e8400-e29b-41d4-a716-446655440000', 77, 1),
('550e8400-e29b-41d4-a716-446655440000', 91, 1),
('550e8400-e29b-41d4-a716-446655440000', 107, 1),
('550e8400-e29b-41d4-a716-446655440000', 108, 1),
('550e8400-e29b-41d4-a716-446655440000', 110, 1),
('550e8400-e29b-41d4-a716-446655440000', 122, 1),
('550e8400-e29b-41d4-a716-446655440000', 124, 1),
('550e8400-e29b-41d4-a716-446655440000', 126, 1),
('550e8400-e29b-41d4-a716-446655440000', 127, 2),
('550e8400-e29b-41d4-a716-446655440000', 129, 1),
('550e8400-e29b-41d4-a716-446655440000', 136, 1),
('550e8400-e29b-41d4-a716-446655440000', 146, 1),
('550e8400-e29b-41d4-a716-446655440000', 149, 2),
('550e8400-e29b-41d4-a716-446655440000', 158, 2),
('550e8400-e29b-41d4-a716-446655440000', 163, 1),
('550e8400-e29b-41d4-a716-446655440000', 165, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `control_sobres`
--

CREATE TABLE `control_sobres` (
  `usuario_id` varchar(36) NOT NULL,
  `sobres_abiertos` int(11) DEFAULT 0,
  `ultima_apertura` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `control_sobres`
--

INSERT INTO `control_sobres` (`usuario_id`, `sobres_abiertos`, `ultima_apertura`) VALUES
('550e8400-e29b-41d4-a716-446655440000', 4, '2026-05-25');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entradas`
--

CREATE TABLE `entradas` (
  `entrada_id` varchar(36) NOT NULL,
  `partido_id` int(11) DEFAULT NULL,
  `usuario_id` varchar(36) DEFAULT NULL,
  `estado` enum('Disponible','Reservada','Pagada','Transferida','Reembolsada','Expirada') DEFAULT 'Disponible',
  `precio` decimal(10,2) DEFAULT NULL,
  `reserva_expira_at` datetime DEFAULT NULL,
  `hash_auditoria` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `laminas`
--

CREATE TABLE `laminas` (
  `lamina_id` int(11) NOT NULL,
  `nombre_jugador` varchar(255) DEFAULT NULL,
  `seleccion` varchar(255) DEFAULT NULL,
  `posicion` varchar(100) DEFAULT NULL,
  `especial` tinyint(1) DEFAULT 0,
  `imagen_url` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `laminas`
--

INSERT INTO `laminas` (`lamina_id`, `nombre_jugador`, `seleccion`, `posicion`, `especial`, `imagen_url`) VALUES
(1, 'Escudo Mexico', 'Mexico', 'Escudo', 0, 'mexico_escudo.png'),
(2, 'Escudo Sudafrica', 'Sudafrica', 'Escudo', 0, 'sudafrica_escudo.png'),
(3, 'Escudo Korea Del Sur', 'Korea Del Sur', 'Escudo', 0, 'korea_del_sur_escudo.png'),
(4, 'Escudo Republica Checa', 'Republica Checa', 'Escudo', 0, 'republica_checa_escudo.png'),
(5, 'Escudo Canada', 'Canada', 'Escudo', 0, 'canada_escudo.png'),
(6, 'Escudo Bosnia y Herzegovina', 'Bosnia y Herzegovina', 'Escudo', 0, 'bosnia_y_herzegovina_escudo.png'),
(7, 'Escudo Qatar', 'Qatar', 'Escudo', 0, 'qatar_escudo.png'),
(8, 'Escudo Suiza', 'Suiza', 'Escudo', 0, 'suiza_escudo.png'),
(9, 'Escudo Brasil', 'Brasil', 'Escudo', 0, 'brasil_escudo.png'),
(10, 'Escudo Marruecos', 'Marruecos', 'Escudo', 0, 'marruecos_escudo.png'),
(11, 'Escudo Haiti', 'Haiti', 'Escudo', 0, 'haiti_escudo.png'),
(12, 'Escudo Escocia', 'Escocia', 'Escudo', 0, 'escocia_escudo.png'),
(13, 'Escudo EEUU', 'EEUU', 'Escudo', 0, 'eeuu_escudo.png'),
(14, 'Escudo Paraguay', 'Paraguay', 'Escudo', 0, 'paraguay_escudo.png'),
(15, 'Escudo Australia', 'Australia', 'Escudo', 0, 'australia_escudo.png'),
(16, 'Escudo Turquia', 'Turquia', 'Escudo', 0, 'turquia_escudo.png'),
(17, 'Escudo Alemania', 'Alemania', 'Escudo', 0, 'alemania_escudo.png'),
(18, 'Escudo Curazao', 'Curazao', 'Escudo', 0, 'curazao_escudo.png'),
(19, 'Escudo Costa de Marfil', 'Costa de Marfil', 'Escudo', 0, 'costa_de_marfil_escudo.png'),
(20, 'Escudo Ecuador', 'Ecuador', 'Escudo', 0, 'ecuador_escudo.png'),
(21, 'Escudo Paises Bajos', 'Paises Bajos', 'Escudo', 0, 'paises_bajos_escudo.png'),
(22, 'Escudo Japon', 'Japon', 'Escudo', 0, 'japon_escudo.png'),
(23, 'Escudo Suecia', 'Suecia', 'Escudo', 0, 'suecia_escudo.png'),
(24, 'Escudo Tunez', 'Tunez', 'Escudo', 0, 'tunez_escudo.png'),
(25, 'Escudo Belgica', 'Belgica', 'Escudo', 0, 'belgica_escudo.png'),
(26, 'Escudo Egipto', 'Egipto', 'Escudo', 0, 'egipto_escudo.png'),
(27, 'Escudo Iran', 'Iran', 'Escudo', 0, 'iran_escudo.png'),
(28, 'Escudo Nueva Zelanda', 'Nueva Zelanda', 'Escudo', 0, 'nueva_zelanda_escudo.png'),
(29, 'Escudo España', 'España', 'Escudo', 0, 'españa_escudo.png'),
(30, 'Escudo Cabo Verde', 'Cabo Verde', 'Escudo', 0, 'cabo_verde_escudo.png'),
(31, 'Escudo Arabia Saudita', 'Arabia Saudita', 'Escudo', 0, 'arabia_saudita_escudo.png'),
(32, 'Escudo Uruguay', 'Uruguay', 'Escudo', 0, 'uruguay_escudo.png'),
(33, 'Escudo Francia', 'Francia', 'Escudo', 0, 'francia_escudo.png'),
(34, 'Escudo Senegal', 'Senegal', 'Escudo', 0, 'senegal_escudo.png'),
(35, 'Escudo Irak', 'Irak', 'Escudo', 0, 'irak_escudo.png'),
(36, 'Escudo Noruega', 'Noruega', 'Escudo', 0, 'noruega_escudo.png'),
(37, 'Escudo Argentina', 'Argentina', 'Escudo', 0, 'argentina_escudo.png'),
(38, 'Escudo Argelia', 'Argelia', 'Escudo', 0, 'argelia_escudo.png'),
(39, 'Escudo Austria', 'Austria', 'Escudo', 0, 'austria_escudo.png'),
(40, 'Escudo Jordania', 'Jordania', 'Escudo', 0, 'jordania_escudo.png'),
(41, 'Escudo Portugal', 'Portugal', 'Escudo', 0, 'portugal_escudo.png'),
(42, 'Escudo Congo', 'Congo', 'Escudo', 0, 'congo_escudo.png'),
(43, 'Escudo Uzbekistan', 'Uzbekistan', 'Escudo', 0, 'uzbekistan_escudo.png'),
(44, 'Escudo Colombia', 'Colombia', 'Escudo', 0, 'colombia_escudo.png'),
(45, 'Escudo Inglaterra', 'Inglaterra', 'Escudo', 0, 'inglaterra_escudo.png'),
(46, 'Escudo Croacia', 'Croacia', 'Escudo', 0, 'croacia_escudo.png'),
(47, 'Escudo Ghana', 'Ghana', 'Escudo', 0, 'ghana_escudo.png'),
(48, 'Escudo Panama', 'Panama', 'Escudo', 0, 'panama_escudo.png'),
(49, 'Emiliano Martinez', 'Argentina', 'Arquero', 0, 'emiliano_martinez.png'),
(50, 'Cristian Romero', 'Argentina', 'Defensa', 0, 'cristian_romero.png'),
(51, 'Nico Paz', 'Argentina', 'Mediocampista', 0, 'nico_paz.png'),
(52, 'Lionel Messi', 'Argentina', 'Delantero', 0, 'lionel_messi.png'),
(53, 'Julian Alvarez', 'Argentina', 'Delantero', 0, 'julian_alvarez.png'),
(54, 'Alisson', 'Brasil', 'Arquero', 0, 'alisson.png'),
(55, 'Marquinhos', 'Brasil', 'Defensa', 0, 'marquinhos.png'),
(57, 'Vinicius Junior', 'Brasil', 'Delantero', 0, 'vinicius_junior.png'),
(58, 'Rodrygo', 'Brasil', 'Delantero', 0, 'rodrygo.png'),
(59, 'Camilo Vargas', 'Colombia', 'Arquero', 0, 'camilo_vargas.png'),
(60, 'Davinson Sanchez', 'Colombia', 'Defensa', 0, 'davinson_sanchez.png'),
(61, 'James Rodríguez', 'Colombia', 'Mediocampista', 0, 'james.png'),
(62, 'Luis Diaz', 'Colombia', 'Delantero', 0, 'luis_diaz.png'),
(64, 'Diogo Costa', 'Portugal', 'Arquero', 0, 'diogo_costa.png'),
(65, 'Ruben Dias', 'Portugal', 'Defensa', 0, 'ruben_dias.png'),
(66, 'Vitinha', 'Portugal', 'Mediocampista', 0, 'vitinha.png'),
(67, 'Cristiano Ronaldo', 'Portugal', 'Delantero', 0, 'cristiano_ronaldo.png'),
(68, 'Rafael Leao', 'Portugal', 'Delantero', 0, 'rafael_leao.png'),
(69, 'Copa del Mundo', 'Especial', 'Especial', 1, 'copa_del_mundo.png'),
(70, 'Balon Oficial', 'Especial', 'Especial', 1, 'balon_oficial.png'),
(71, 'Mascota Mundial', 'Especial', 'Especial', 1, 'mascota_mundial.png'),
(73, 'Logo Mundial', 'Especial', 'Especial', 1, 'logo_mundial.png'),
(74, 'Lionel Messi Extra', 'Especial', 'Especial', 1, 'lionel_messi_extra.png'),
(75, 'Thibaut Courtois Extra', 'Especial', 'Especial', 1, 'courtois_extra.png'),
(76, 'Federico Valverde Extra', 'Especial', 'Especial', 1, 'valverde_extra.png'),
(77, 'Luis Diaz Extra', 'Especial', 'Especial', 1, 'luis_diaz_extra.png'),
(78, 'Luka Modric Extra', 'Especial', 'Especial', 1, 'luka_modric_extra.png'),
(79, 'Lamine Yamal Extra', 'Especial', 'Especial', 1, 'lamine_yamal_extra.png'),
(80, 'Cristiano Ronaldo Extra', 'Especial', 'Especial', 1, 'ronaldo_extra.png'),
(81, 'Kylian Mbappe Extra', 'Especial', 'Especial', 1, 'kylian_mbappe_extra.png'),
(82, 'Mohamed Salah Extra', 'Especial', 'Especial', 1, 'mohamed_salah_extra.png'),
(83, 'Erling Haaland Extra', 'Especial', 'Especial', 1, 'erling_haaland_extra.png'),
(91, 'Bruno Guimaraes', 'Brasil', 'Mediocampista', 0, 'bruno_guimaraes.png'),
(97, 'Jhon Arias', 'Colombia', 'Delantero', 0, 'jhon_arias.png'),
(104, 'Mike Maignan', 'Francia', 'Arquero', 0, 'mike_maignan.png'),
(105, 'William Saliba', 'Francia', 'Defensa', 0, 'william_saliba.png'),
(106, 'Michael Olise', 'Francia', 'Mediocampista', 0, 'olise.png'),
(107, 'Ousmane Dembele', 'Francia', 'Delantero', 0, 'ousmane_dembele.png'),
(108, 'Kylian Mbappe', 'Francia', 'Delantero', 0, 'kylian_mbappe.png'),
(109, 'Jordan Pickford', 'Inglaterra', 'Arquero', 0, 'jordan_pickford.png'),
(110, 'Declan Rice', 'Inglaterra', 'Mediocampista', 0, 'declan_rice.png'),
(111, 'Jude Bellingham', 'Inglaterra', 'Mediocampista', 0, 'jude_bellingham.png'),
(112, 'Marcus Rashford', 'Inglaterra', 'Delantero', 0, 'rashford.png'),
(113, 'Harry Kane', 'Inglaterra', 'Delantero', 0, 'harry_kane.png'),
(114, 'Unai Simon', 'España', 'Arquero', 0, 'unai_simon.png'),
(115, 'Rodri', 'España', 'Mediocampista', 0, 'rodri.png'),
(116, 'Pedri', 'España', 'Mediocampista', 0, 'pedri.png'),
(117, 'Nico Williams', 'España', 'Delantero', 0, 'nico_williams.png'),
(118, 'Lamine Yamal', 'España', 'Delantero', 0, 'lamine_yamal.png'),
(119, 'Marc Andre ter Stegen', 'Alemania', 'Arquero', 0, 'ter_stegen.png'),
(120, 'Antonio Rudiger', 'Alemania', 'Defensa', 0, 'antonio_rudiger.png'),
(121, 'Jamal Musiala', 'Alemania', 'Mediocampista', 0, 'musiala.png'),
(122, 'Florian Wirtz', 'Alemania', 'Mediocampista', 0, 'wirtz.png'),
(123, 'Kai Havertz', 'Alemania', 'Delantero', 0, 'havertz.png'),
(124, 'Sergio Rochet', 'Uruguay', 'Arquero', 0, 'sergio_rochet.png'),
(125, 'Ronald Araujo', 'Uruguay', 'Defensa', 0, 'ronald_araujo.png'),
(126, 'Federico Valverde', 'Uruguay', 'Mediocampista', 0, 'federico_valverde.png'),
(127, 'Darwin Nunez', 'Uruguay', 'Delantero', 0, 'darwin_nunez.png'),
(128, 'Giorgian De Arrascaeta', 'Uruguay', 'Mediocampista', 0, 'de_arrascaeta.png'),
(129, 'Thibaut Courtois', 'Belgica', 'Arquero', 0, 'courtois.png'),
(130, 'Thomas Meunier', 'Belgica', 'Defensa', 0, 'meunier.png'),
(131, 'Kevin De Bruyne', 'Belgica', 'Mediocampista', 0, 'kevin_de_bruyne.png'),
(132, 'Jeremy Doku', 'Belgica', 'Delantero', 0, 'jeremy_doku.png'),
(133, 'Romelu Lukaku', 'Belgica', 'Delantero', 0, 'romelu_lukaku.png'),
(134, 'Bart Verbruggen', 'Paises Bajos', 'Arquero', 0, 'bart_verbruggen.png'),
(135, 'Virgil van Dijk', 'Paises Bajos', 'Defensa', 0, 'virgil_van_dijk.png'),
(136, 'Frenkie de Jong', 'Paises Bajos', 'Mediocampista', 0, 'frenkie_de_jong.png'),
(137, 'Xavi Simons', 'Paises Bajos', 'Mediocampista', 0, 'xavi_simons.png'),
(138, 'Memphis Depay', 'Paises Bajos', 'Delantero', 0, 'depay.png'),
(139, 'Dominik Livakovic', 'Croacia', 'Arquero', 0, 'dominik_livakovic.png'),
(140, 'Josko Gvardiol', 'Croacia', 'Defensa', 0, 'josko_gvardiol.png'),
(141, 'Luka Modric', 'Croacia', 'Mediocampista', 0, 'luka_modric.png'),
(142, 'Mateo Kovacic', 'Croacia', 'Mediocampista', 0, 'mateo_kovacic.png'),
(143, 'Andrej Kramaric', 'Croacia', 'Delantero', 0, 'andrej_kramaric.png'),
(144, 'Yassine Bounou', 'Marruecos', 'Arquero', 0, 'yassine_bounou.png'),
(145, 'Achraf Hakimi', 'Marruecos', 'Defensa', 0, 'hakimi.png'),
(146, 'Sofyan Amrabat', 'Marruecos', 'Mediocampista', 0, 'amrabat.png'),
(147, 'Abde Ezzalzouli', 'Marruecos', 'Delantero', 0, 'abde.png'),
(148, 'Youssef En-Nesyri', 'Marruecos', 'Delantero', 0, 'nesyri.png'),
(149, 'Luis Malagon', 'Mexico', 'Arquero', 0, 'luis_malagon.png'),
(150, 'Cesar Montes', 'Mexico', 'Defensa', 0, 'cesar_montes.png'),
(151, 'Edson Alvarez', 'Mexico', 'Mediocampista', 0, 'edson_alvarez.png'),
(152, 'Santiago Gimenez', 'Mexico', 'Delantero', 0, 'santiago_gimenez.png'),
(153, 'Hirving Lozano', 'Mexico', 'Delantero', 0, 'hirving_lozano.png'),
(154, 'Matt Freese', 'EEUU', 'Arquero', 0, 'matt_freese.png'),
(155, 'Weston McKennie', 'EEUU', 'Mediocampista', 0, 'mckennie.png'),
(156, 'Diego Luna', 'EEUU', 'Mediocampista', 0, 'diego_luna.png'),
(157, 'Christian Pulisic', 'EEUU', 'Delantero', 0, 'pulisic.png'),
(158, 'Timothy Weah', 'EEUU', 'Delantero', 0, 'weah.png'),
(159, 'Orjan Nyland', 'Noruega', 'Arquero', 0, 'orjan_nyland.png'),
(160, 'Martin Odegaard', 'Noruega', 'Mediocampista', 0, 'martin_odegaard.png'),
(161, 'Sander Berge', 'Noruega', 'Mediocampista', 0, 'sander_berge.png'),
(162, 'Erling Haaland', 'Noruega', 'Delantero', 0, 'erling_haaland.png'),
(163, 'Alexander Sorloth', 'Noruega', 'Delantero', 0, 'alexander_sorloth.png'),
(164, 'Mohamed El Shenawy', 'Egipto', 'Arquero', 0, 'mohamed_el_shenawy.png'),
(165, 'Mohamed Hamdy', 'Egipto', 'Defensa', 0, 'hamdy.png'),
(166, 'Trezeguet', 'Egipto', 'Mediocampista', 0, 'trezeguet.png'),
(167, 'Omar Marmoush', 'Egipto', 'Delantero', 0, 'omar_marmoush.png'),
(168, 'Mohamed Salah', 'Egipto', 'Delantero', 0, 'mohamed_salah.png'),
(184, 'Nawaf Alaqidi', 'Arabia Saudita', 'Portero', 0, 'nawaf_alaqidi.png'),
(185, 'Jehad Thikri', 'Arabia Saudita', 'Defensa', 0, 'jehad_thikri.png'),
(186, 'Saud Abdulhamid', 'Arabia Saudita', 'Defensa', 0, 'saud_abdulhamid.png'),
(187, 'Ziyad Aljohani', 'Arabia Saudita', 'Mediocampista', 0, 'ziyad_aljohani.png'),
(188, 'Salem Aldawsari', 'Arabia Saudita', 'Delantero', 0, 'salem_aldawsari.png'),
(189, 'Alexis Guendouz', 'Argelia', 'Portero', 0, 'alexis_guendouz.png'),
(190, 'Youcef Atal', 'Argelia', 'Defensa', 0, 'youcef_atal.png'),
(191, 'Ramy Bensebaini', 'Argelia', 'Defensa', 0, 'ramy_bensebaini.png'),
(192, 'Houssem Aour', 'Argelia', 'Mediocampista', 0, 'houssem_aour.png'),
(193, 'Riyad Mahrez', 'Argelia', 'Delantero', 0, 'riyad_mahrez.png'),
(194, 'Mathew Ryan', 'Australia', 'Portero', 0, 'mathew_ryan.png'),
(195, 'Aziz Behich', 'Australia', 'Defensa', 0, 'aziz_behich.png'),
(196, 'Cameron Burgess', 'Australia', 'Defensa', 0, 'cameron_burgess.png'),
(197, 'Jackson Irvine', 'Australia', 'Mediocampista', 0, 'jackson_irvine.png'),
(198, 'Mohamed Toure', 'Australia', 'Delantero', 0, 'mohamed_toure.png'),
(199, 'Patrick Pentz', 'Austria', 'Portero', 0, 'patrick_pentz.png'),
(200, 'David Alaba', 'Austria', 'Defensa', 0, 'david_alaba.png'),
(201, 'Kevin Danso', 'Austria', 'Defensa', 0, 'kevin_danso.png'),
(202, 'Marcel Sabitzer', 'Austria', 'Mediocampista', 0, 'marcel_sabitzer.png'),
(203, 'Marko Arnautovic', 'Austria', 'Delantero', 0, 'marko_arnautovic.png'),
(204, 'Nikola Vasilj', 'Bosnia y Herzegovina', 'Portero', 0, 'nikola_vasilj.png'),
(205, 'Amar Dedic', 'Bosnia y Herzegovina', 'Defensa', 0, 'amar_dedic.png'),
(206, 'Ivan Basic', 'Bosnia y Herzegovina', 'Defensa', 0, 'ivan_basic.png'),
(207, 'Dzenis Burnic', 'Bosnia y Herzegovina', 'Mediocampista', 0, 'dzenis_burnic.png'),
(208, 'Edin Dzeko', 'Bosnia y Herzegovina', 'Delantero', 0, 'edin_dzeko.png'),
(209, 'Vozinha', 'Cabo Verde', 'Portero', 0, 'vozinha.png'),
(210, 'Diney', 'Cabo Verde', 'Defensa', 0, 'diney.png'),
(211, 'Logan Costa', 'Cabo Verde', 'Defensa', 0, 'logan_costa.png'),
(212, 'Joao Paulo', 'Cabo Verde', 'Mediocampista', 0, 'joao_paulo.png'),
(213, 'Bebe', 'Cabo Verde', 'Delantero', 0, 'bebe.png'),
(214, 'Lionel Mpasi', 'Congo', 'Portero', 0, 'lionel_mpasi.png'),
(215, 'Aaron Wan-Bissaka', 'Congo', 'Defensa', 0, 'aaron_wan-bissaka.png'),
(216, 'Axel Tuanzebe', 'Congo', 'Defensa', 0, 'axel_tuanzebe.png'),
(217, 'Edo Kayembe', 'Congo', 'Mediocampista', 0, 'edo_kayembe.png'),
(218, 'Brian Cipenga', 'Congo', 'Delantero', 0, 'brian_cipenga.png'),
(219, 'Yahia Fofana', 'Costa de Marfil', 'Portero', 0, 'yahia_fofana.png'),
(220, 'Evan Ndicka', 'Costa de Marfil', 'Defensa', 0, 'evan_ndicka.png'),
(221, 'Seko Fofana', 'Costa de Marfil', 'Mediocampista', 0, 'seko_fofana.png'),
(222, 'Franck Kessie', 'Costa de Marfil', 'Mediocampista', 0, 'franck_kessie.png'),
(223, 'Sebastian Haller', 'Costa de Marfil', 'Delantero', 0, 'sebastian_haller.png'),
(224, 'Eloy Room', 'Curazao', 'Portero', 0, 'eloy_room.png'),
(225, 'Shurandy Sambo', 'Curazao', 'Defensa', 0, 'shurandy_sambo.png'),
(226, 'Jurien Gaari', 'Curazao', 'Defensa', 0, 'jurien_gaari.png'),
(227, 'Juninho Bacuna', 'Curazao', 'Mediocampista', 0, 'juninho_bacuna.png'),
(228, 'Jurgen Locadia', 'Curazao', 'Delantero', 0, 'jurgen_locadia.png'),
(229, 'Hernan Galindez', 'Ecuador', 'Portero', 0, 'hernan_galindez.png'),
(230, 'Willian Pacho', 'Ecuador', 'Defensa', 0, 'willian_pacho.png'),
(231, 'Piero Hincapie', 'Ecuador', 'Defensa', 0, 'piero_hincapie.png'),
(232, 'Moises Caicedo', 'Ecuador', 'Mediocampista', 0, 'moises_caicedo.png'),
(233, 'Enner Valencia', 'Ecuador', 'Delantero', 0, 'enner_valencia.png'),
(234, 'Angus Gunn', 'Escocia', 'Portero', 0, 'angus_gunn.png'),
(235, 'Andrew Robertson', 'Escocia', 'Defensa', 0, 'andrew_robertson.png'),
(236, 'John McGinn', 'Escocia', 'Mediocampista', 0, 'john_mcginn.png'),
(237, 'Scott McTominay', 'Escocia', 'Mediocampista', 0, 'scott_mctominay.png'),
(238, 'Lyndon Dykes', 'Escocia', 'Delantero', 0, 'lyndon_dykes.png'),
(239, 'Lawrence Ati Zigi', 'Ghana', 'Portero', 0, 'lawrence_ati_zigi.png'),
(240, 'Gideon Mensah', 'Ghana', 'Defensa', 0, 'gideon_mensah.png'),
(241, 'Thomas Partey', 'Ghana', 'Mediocampista', 0, 'thomas_partey.png'),
(242, 'Antoine Semenyo', 'Ghana', 'Delantero', 0, 'antoine_semenyo.png'),
(243, 'Mohammed Kudus', 'Ghana', 'Delantero', 0, 'mohammed_kudus.png'),
(244, 'Johny Placide', 'Haiti', 'Portero', 0, 'johny_placide.png'),
(245, 'Duke Lacroix', 'Haiti', 'Defensa', 0, 'duke_lacroix.png'),
(246, 'Ricardo Ade', 'Haiti', 'Defensa', 0, 'ricardo_ade.png'),
(248, 'Ruben Providence', 'Haiti', 'Delantero', 0, 'ruben_providence.png'),
(249, 'Jalal Hasan', 'Irak', 'Portero', 0, 'jalal_hasan.png'),
(250, 'Merchas Doski', 'Irak', 'Defensa', 0, 'merchas_doski.png'),
(251, 'Rebin Sulaka', 'Irak', 'Defensa', 0, 'rebin_sulaka.png'),
(252, 'Youssef Amyn', 'Irak', 'Mediocampista', 0, 'youssef_amyn.png'),
(253, 'Ali Al-Hamadi', 'Irak', 'Delantero', 0, 'ali_alhamadi.png'),
(254, 'Alireza Beiranvand', 'Iran', 'Portero', 0, 'alireza_beiranvand.png'),
(255, 'Saleh Hardani', 'Iran', 'Defensa', 0, 'saleh_hardani.png'),
(256, 'Saman Ghoddos', 'Iran', 'Mediocampista', 0, 'saman_ghoddos.png'),
(257, 'Mohammad Mohebi', 'Iran', 'Mediocampista', 0, 'mohammad_mohebi.png'),
(258, 'Ali Gholizadeh', 'Iran', 'Delantero', 0, 'ali_gholizadeh.png'),
(259, 'Zion Suzuki', 'Japon', 'Portero', 0, 'zion_suzuki.png'),
(260, 'Ayumi Seko', 'Japon', 'Defensa', 0, 'ayumi_seko.png'),
(261, 'Kaishu Sano', 'Japon', 'Mediocampista', 0, 'kaishu_sano.png'),
(262, 'Takumi Minamino', 'Japon', 'Mediocampista', 0, 'takumi_minamino.png'),
(263, 'Junya Ito', 'Japon', 'Delantero', 0, 'junya_ito.png'),
(264, 'Yazeed Abulaila', 'Jordania', 'Portero', 0, 'yazeed_abulaila.png'),
(265, 'Saleem Obaid', 'Jordania', 'Defensa', 0, 'saleem_obaid.png'),
(266, 'Abdallah Nasib', 'Jordania', 'Defensa', 0, 'abdallah_nasib.png'),
(267, 'Amer Jamous', 'Jordania', 'Mediocampista', 0, 'amer_jamous.png'),
(268, 'Ibrahim Sabra', 'Jordania', 'Delantero', 0, 'ibrahim_sabra.png'),
(269, 'Alex Paulsen', 'Nueva Zelanda', 'Portero', 0, 'alex_paulsen.png'),
(270, 'Michael Boxall', 'Nueva Zelanda', 'Defensa', 0, 'michael_boxall.png'),
(271, 'Ryan Thomas', 'Nueva Zelanda', 'Mediocampista', 0, 'ryan_thomas.png'),
(272, 'Matthew Garbett', 'Nueva Zelanda', 'Mediocampista', 0, 'matthew_garbett.png'),
(273, 'Chris Wood', 'Nueva Zelanda', 'Delantero', 0, 'chris_wood.png'),
(274, 'Luis Mejia', 'Panama', 'Portero', 0, 'luis_mejia.png'),
(275, 'Cesar Blackman', 'Panama', 'Defensa', 0, 'cesar_blackman.png'),
(276, 'Jose Cordoba', 'Panama', 'Defensa', 0, 'jose_cordoba.png'),
(277, 'Anibal Godoy', 'Panama', 'Mediocampista', 0, 'anibal_godoy.png'),
(278, 'Jose Luis Rodriguez', 'Panama', 'Delantero', 0, 'jose_luis_rodriguez.png'),
(279, 'Orlando Gill', 'Paraguay', 'Portero', 0, 'orlando_gill.png'),
(280, 'Omar Alderete', 'Paraguay', 'Defensa', 0, 'omar_alderete.png'),
(281, 'Julio Enciso', 'Paraguay', 'Mediocampista', 0, 'julio_enciso.png'),
(282, 'Miguel Almiron', 'Paraguay', 'Delantero', 0, 'miguel_almiron.png'),
(283, 'Angel Romero', 'Paraguay', 'Delantero', 0, 'angel_romero.png'),
(284, 'Meshaal Barsham', 'Qatar', 'Portero', 0, 'meshaal_barsham.png'),
(285, 'Pedro Miguel', 'Qatar', 'Defensa', 0, 'pedro_miguel.png'),
(286, 'Mohammed Mannai', 'Qatar', 'Mediocampista', 0, 'mohammed_mannai.png'),
(287, 'Assim Madibo', 'Qatar', 'Mediocampista', 0, 'assim_madibo.png'),
(288, 'Hassan Afif', 'Qatar', 'Delantero', 0, 'hassan_afif.png'),
(289, 'Edouard Mendy', 'Senegal', 'Portero', 0, 'edouard_mendy.png'),
(290, 'Kalidou Koulibaly', 'Senegal', 'Defensa', 0, 'kalidou_koulibaly.png'),
(291, 'Pape Matar Sarr', 'Senegal', 'Mediocampista', 0, 'pape_matar_sarr.png'),
(292, 'Sadio Mane', 'Senegal', 'Delantero', 0, 'sadio_mane.png'),
(293, 'Nicolas Jackson', 'Senegal', 'Delantero', 0, 'nicolas_jackson.png'),
(294, 'Viktor Johansson', 'Suecia', 'Portero', 0, 'viktor_johansson.png'),
(295, 'Lucas Bergvall', 'Suecia', 'Mediocampista', 0, 'lucas_bergvall.png'),
(296, 'Roony Bardghji', 'Suecia', 'Delantero', 0, 'roony_bardghji.png'),
(297, 'Antony Elanga', 'Suecia', 'Delantero', 0, 'antony_elanga.png'),
(298, 'Viktor Gyokeres', 'Suecia', 'Delantero', 0, 'viktor_gyokeres.png'),
(299, 'Gregor Kobel', 'Suiza', 'Portero', 0, 'gregor_kobel.png'),
(300, 'Manuel Akanji', 'Suiza', 'Defensa', 0, 'manuel_akanji.png'),
(301, 'Granit Xhaka', 'Suiza', 'Mediocampista', 0, 'granit_xhaka.png'),
(302, 'Denis Zakaria', 'Suiza', 'Mediocampista', 0, 'denis_zakaria.png'),
(303, 'Breel Embolo', 'Suiza', 'Delantero', 0, 'breel_embolo.png'),
(304, 'Bechir Ben Said', 'Tunez', 'Portero', 0, 'bechir_ben_said.png'),
(305, 'Ali Abdi', 'Tunez', 'Defensa', 0, 'ali_abdi.png'),
(306, 'Yassine Meriah', 'Tunez', 'Defensa', 0, 'yassine_meriah.png'),
(307, 'Hannibal Mejbri', 'Tunez', 'Mediocampista', 0, 'hannibal_mejbri.png'),
(308, 'Elias Saad', 'Tunez', 'Delantero', 0, 'elias_saad.png'),
(309, 'Ugurcan Cakir', 'Turquia', 'Portero', 0, 'ugurcan_cakir.png'),
(310, 'Caglar Soyuncu', 'Turquia', 'Defensa', 0, 'caglar_soyuncu.png'),
(311, 'Orkun Kokcu', 'Turquia', 'Mediocampista', 0, 'orkun_kokcu.png'),
(312, 'Kenan Yildiz', 'Turquia', 'Delantero', 0, 'kenan_yildiz.png'),
(313, 'Arda Guler', 'Turquia', 'Delantero', 0, 'arda_guler.png'),
(314, 'Utkit Yusupov', 'Uzbekistan', 'Portero', 0, 'utkit_yusupov.png'),
(315, 'Abdukodir Khusanov', 'Uzbekistan', 'Defensa', 0, 'abdukodir_khusanov.png'),
(316, 'Otabek Shukurov', 'Uzbekistan', 'Mediocampista', 0, 'otabek_shukurov.png'),
(317, 'Jamshid Iskanderov', 'Uzbekistan', 'Mediocampista', 0, 'jamshid_iskanderov.png'),
(318, 'Eldor Shomurodov', 'Uzbekistan', 'Delantero', 0, 'eldor_shomurodov.png'),
(319, 'Sipho Chaine', 'Sudafrica', 'Portero', 0, 'sipho_chaine.png'),
(320, 'Samukele Kabini', 'Sudafrica', 'Defensa', 0, 'samukele_kabini.png'),
(321, 'Bathusi Aubaas', 'Sudafrica', 'Mediocampista', 0, 'bathusi_aubaas.png'),
(322, 'Iqraam Rayners', 'Sudafrica', 'Delantero', 0, 'iqraam_rayners.png'),
(323, 'Lyle Foster', 'Sudafrica', 'Delantero', 0, 'lyle_foster.png'),
(324, 'Seunggyu Kum', 'Korea del Sur', 'Portero', 0, 'seunggyu_kum.png'),
(325, 'Minjae Kim', 'Korea del Sur', 'Defensa', 0, 'minjae_kim.png'),
(326, 'Hanbeom Lee', 'Korea del Sur', 'Defensa', 0, 'hanbeom_lee.png'),
(327, 'Kangin Lee', 'Korea del Sur', 'Mediocampista', 0, 'kangin_lee.png'),
(328, 'Heungmin Son', 'Korea del Sur', 'Delantero', 0, 'heungmin_son.png'),
(329, 'Matej Kovar', 'Republica Checa', 'Portero', 0, 'matej_kovar.png'),
(330, 'Tomas Holes', 'Republica Checa', 'Defensa', 0, 'tomas_holes.png'),
(331, 'Vladimir Coufal', 'Republica Checa', 'Defensa', 0, 'vladimir_coufal.png'),
(332, 'Tomas Soucek', 'Republica Checa', 'Mediocampista', 0, 'tomas_soucek.png'),
(333, 'Patrik Schick', 'Republica Checa', 'Delantero', 0, 'patrik_schick.png'),
(334, 'Dayne St. Clair', 'Canada', 'Portero', 0, 'dayne_st_clair.png'),
(335, 'Alphonso Davies', 'Canada', 'Defensa', 0, 'alphonso_davies.png'),
(337, 'Moise Bombito', 'Canada', 'Mediocampista', 0, 'moise_bombito.png'),
(338, 'Jonathan David', 'Canada', 'Delantero', 0, 'jonathan_david.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partidos`
--

CREATE TABLE `partidos` (
  `partido_id` int(11) NOT NULL,
  `equipo_a` varchar(50) NOT NULL,
  `equipo_b` varchar(50) NOT NULL,
  `fecha_hora` datetime NOT NULL,
  `estadio` varchar(100) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `fase` varchar(50) DEFAULT NULL,
  `estado` enum('programado','en juego','finalizado') DEFAULT 'programado',
  `resultado_a` int(11) DEFAULT 0,
  `resultado_b` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pollas_grupos`
--

CREATE TABLE `pollas_grupos` (
  `grupo_id` int(11) NOT NULL,
  `nombre_grupo` varchar(100) NOT NULL,
  `codigo_invitacion` varchar(10) NOT NULL,
  `creador_id` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pronosticos`
--

CREATE TABLE `pronosticos` (
  `pronostico_id` int(11) NOT NULL,
  `usuario_id` varchar(36) DEFAULT NULL,
  `partido_id` int(11) DEFAULT NULL,
  `grupo_id` int(11) DEFAULT NULL,
  `goles_a` int(11) NOT NULL,
  `goles_b` int(11) NOT NULL,
  `puntos_obtenidos` int(11) DEFAULT 0,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario_id` varchar(36) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password_hash` text NOT NULL,
  `puntos_totales` int(11) DEFAULT 0,
  `saldo` decimal(12,2) DEFAULT 0.00,
  `rol` enum('aficionado','operador','soporte') DEFAULT 'aficionado',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usuario_id`, `nombre`, `email`, `password_hash`, `puntos_totales`, `saldo`, `rol`, `created_at`) VALUES
('550e8400-e29b-41d4-a716-446655440000', 'Sebastian', 'sebas@test.com', '123456', 0, 9999985999.99, 'aficionado', '2026-05-20 20:21:20');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `coleccion_usuario`
--
ALTER TABLE `coleccion_usuario`
  ADD PRIMARY KEY (`usuario_id`,`lamina_id`),
  ADD KEY `lamina_id` (`lamina_id`);

--
-- Indices de la tabla `control_sobres`
--
ALTER TABLE `control_sobres`
  ADD PRIMARY KEY (`usuario_id`);

--
-- Indices de la tabla `entradas`
--
ALTER TABLE `entradas`
  ADD PRIMARY KEY (`entrada_id`),
  ADD KEY `partido_id` (`partido_id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `laminas`
--
ALTER TABLE `laminas`
  ADD PRIMARY KEY (`lamina_id`);

--
-- Indices de la tabla `partidos`
--
ALTER TABLE `partidos`
  ADD PRIMARY KEY (`partido_id`);

--
-- Indices de la tabla `pollas_grupos`
--
ALTER TABLE `pollas_grupos`
  ADD PRIMARY KEY (`grupo_id`),
  ADD UNIQUE KEY `codigo_invitacion` (`codigo_invitacion`),
  ADD KEY `creador_id` (`creador_id`);

--
-- Indices de la tabla `pronosticos`
--
ALTER TABLE `pronosticos`
  ADD PRIMARY KEY (`pronostico_id`),
  ADD UNIQUE KEY `pronostico_unico` (`usuario_id`,`partido_id`,`grupo_id`),
  ADD KEY `partido_id` (`partido_id`),
  ADD KEY `grupo_id` (`grupo_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usuario_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `laminas`
--
ALTER TABLE `laminas`
  MODIFY `lamina_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=339;

--
-- AUTO_INCREMENT de la tabla `partidos`
--
ALTER TABLE `partidos`
  MODIFY `partido_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pollas_grupos`
--
ALTER TABLE `pollas_grupos`
  MODIFY `grupo_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pronosticos`
--
ALTER TABLE `pronosticos`
  MODIFY `pronostico_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `coleccion_usuario`
--
ALTER TABLE `coleccion_usuario`
  ADD CONSTRAINT `coleccion_usuario_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`),
  ADD CONSTRAINT `coleccion_usuario_ibfk_2` FOREIGN KEY (`lamina_id`) REFERENCES `laminas` (`lamina_id`);

--
-- Filtros para la tabla `control_sobres`
--
ALTER TABLE `control_sobres`
  ADD CONSTRAINT `control_sobres_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`);

--
-- Filtros para la tabla `entradas`
--
ALTER TABLE `entradas`
  ADD CONSTRAINT `entradas_ibfk_1` FOREIGN KEY (`partido_id`) REFERENCES `partidos` (`partido_id`),
  ADD CONSTRAINT `entradas_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`);

--
-- Filtros para la tabla `pollas_grupos`
--
ALTER TABLE `pollas_grupos`
  ADD CONSTRAINT `pollas_grupos_ibfk_1` FOREIGN KEY (`creador_id`) REFERENCES `usuarios` (`usuario_id`);

--
-- Filtros para la tabla `pronosticos`
--
ALTER TABLE `pronosticos`
  ADD CONSTRAINT `pronosticos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`),
  ADD CONSTRAINT `pronosticos_ibfk_2` FOREIGN KEY (`partido_id`) REFERENCES `partidos` (`partido_id`),
  ADD CONSTRAINT `pronosticos_ibfk_3` FOREIGN KEY (`grupo_id`) REFERENCES `pollas_grupos` (`grupo_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
