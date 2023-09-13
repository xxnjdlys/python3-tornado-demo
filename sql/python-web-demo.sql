SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for python-test
-- ----------------------------
DROP TABLE IF EXISTS `python-test`;
CREATE TABLE `python-test`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of python-test
-- ----------------------------
INSERT INTO `python-test` VALUES (1, '嘿嘿嘿', '2000-01-01 00:00:00', NULL);
INSERT INTO `python-test` VALUES (2, '哈哈哈', '2000-01-01 00:00:00', NULL);

SET FOREIGN_KEY_CHECKS = 1;
