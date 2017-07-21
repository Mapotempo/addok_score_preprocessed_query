# Addok Score Preprocessed Query

[Addok](https://github.com/etalab/addok) plugin to score the result again the preprocessed query and not the original one.

## Addressed problem

Address can contain oblivious mistake or garbage data we are able to clean on preprocessing step. But the scoring in Addok is make on the input query. With a same address result, longer is the input query, lesser is the score.

### Clean address
`query=7 Rue de la Bergerie, Salleboeuf`
```json
"geocoding": {
  "score": 0.9112636363636362,
  "type": "house",
  "name": "7 Rue de la Bergerie",
}
```

### With garbage
`query=7 Rue de la Bergerie (passer par l'arrière), Salleboeuf`
```json
"geocoding": {
  "score": 0.5369320855614973,
  "type": "house",
  "name": "7 Rue de la Bergerie",
}
```

## Configuration

Add `addok_score_preprocessed_query.score_preprocessed_query` in first place into `SEARCH_RESULT_PROCESSORS_PYPATHS`.

```
SEARCH_RESULT_PROCESSORS_PYPATHS = [
    'addok_score_preprocessed_query.score_preprocessed_query',
    ...
```

## How it works

It replaces the query by the preprocessed one just before scoring the result.
