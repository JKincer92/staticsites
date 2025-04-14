import unittest

from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType, Enum


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_single_delimiter(self):
        node = TextNode("This is a **bold** phrase", TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" phrase", TextType.TEXT))

    def test_no_delimiters(self):
        node = TextNode("This has no delimiters", TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("This has no delimiters", TextType.TEXT))

    def test_non_text_node(self):
        node = TextNode("Non-text node should pass unchanged", TextType.BOLD)
        old_nodes = [node]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], node)

    def multiple_old_nodes(self):
        node1 = TextNode("This is a **bold** phrase", TextType.TEXT)
        node2 = TextNode("This is an _italic_ phrase", TextType.TEXT)
        node3 = TextNode("This is an `inline code` phrase", TextType.TEXT)
        old_nodes = [node1, node2, node3]

        nodes_after_bold = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        nodes_after_italic = split_nodes_delimiter(nodes_after_bold, "_", TextType.ITALIC)
        final_nodes = split_nodes_delimiter(nodes_after_italic, "`", TextType.CODE)

        expected_output = [
        TextNode("This is a", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" phrase", TextType.TEXT),
        TextNode("This is an", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" phrase", TextType.TEXT),
        TextNode("This is an ", TextType.TEXT),
        TextNode("inline code", TextType.CODE),
        TextNode(" phrase", TextType.TEXT)
        ]

        assert len(final_nodes) == len(expected_output)
        for generated, expected in zip(final_nodes, expected_output):
            assert generated.text == expected.text
            assert generated.text_type == expected.text_type

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ],
            new_nodes
        )
