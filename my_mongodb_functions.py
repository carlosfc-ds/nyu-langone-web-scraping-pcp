def project_docs(docs, projection):
    """
    Simulate MongoDB projection on a list of dicts.

    docs: List[Dict] - list of documents (dicts)
    projection: Dict[str, int] - dict of fields to include (1) or exclude (0)

    Returns a list of dicts with fields projected
    """
    include_fields = {k for k, v in projection.items() if v}
    exclude_fields = {k for k, v in projection.items() if not v}
    
    if include_fields:
        # Include only specified fields
        return [{k: doc[k] for k in include_fields if k in doc} for doc in docs]
    elif exclude_fields:
        # Exclude specified fields
        return [{k: v for k, v in doc.items() if k not in exclude_fields} for doc in docs]
    else:
        # No projection, return full docs
        return docs