
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
            if self.tag is None:
                return self.value or ""
            if self.value is None and self.children is None:
                return f"<{self.tag}{self.props_to_html()}/>"
            html = f"<{self.tag}{self.props_to_html()}>"
            if self.value is not None:
                html += self.value
            if self.children is not None:
                for child in self.children:
                    html += child.to_html()
            html += f"</{self.tag}>"
    
    def props_to_html(self):
       if self.props is None:
           return ""
       props_html = ""
       for prop in self.props:
           props_html += f' {prop}="{self.props[prop]}"'
       return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Error: Leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node requires a tag")
        if self.children is None:
            raise ValueError("Parent Node must have children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        

