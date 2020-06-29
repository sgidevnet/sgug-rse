-- Convenience Lua functions that can be used within Python srpm/rpm macros

-- Determine alternate names provided from the given name.
-- Used in pythonname provides generator, python_provide and py_provides.
-- There are 2 rules:
--  python3-foo  -> python-foo, python3X-foo
--  python3X-foo -> python-foo, python3-foo
-- There is no python-foo -> rule, python-foo packages are version agnostic.
-- Returns a table/array with strings. Empty when no rule matched.
local function python_altnames(name)
  local xy = rpm.expand('%{__default_python3_pkgversion}')
  local altnames = {}
  local replaced
  -- NB: dash needs to be escaped!
  if name:match('^python3%-') then
    for i, prefix in ipairs({'python-', 'python' .. xy .. '-'}) do
      replaced = name:gsub('^python3%-', prefix)
      table.insert(altnames, replaced)
    end
  elseif name:match('^python' .. xy .. '%-') then
    for i, prefix in ipairs({'python-', 'python3-'}) do
      replaced = name:gsub('^python' .. xy .. '%-', prefix)
      table.insert(altnames, replaced)
    end
  end
  return altnames
end


-- For any given name and epoch-version-release, return provides except self.
-- Uses python_altnames under the hood
-- Returns a table/array with strings.
local function python_altprovides(name, evr)
  -- global cache that tells what provides were already processed
  if __python_altnames_provides_beenthere == nil then
    __python_altnames_provides_beenthere = {}
  end
  __python_altnames_provides_beenthere[name .. ' ' .. evr] = true
  local altprovides = {}
  for i, altname in ipairs(python_altnames(name)) do
    table.insert(altprovides, altname .. ' = ' .. evr)
  end
  return altprovides
end


-- Like python_altprovides but only return something once.
-- For each argument can only be used once, returns nil otherwise.
-- Previous usage of python_altprovides counts as well.
local function python_altprovides_once(name, evr)
  -- global cache that tells what provides were already processed
  if __python_altnames_provides_beenthere == nil then
    __python_altnames_provides_beenthere = {}
  end
  if __python_altnames_provides_beenthere[name .. ' ' .. evr] == nil then
    __python_altnames_provides_beenthere[name .. ' ' .. evr] = true
    return python_altprovides(name, evr)
  else
    return nil
  end
end


return {
  python_altnames = python_altnames,
  python_altprovides = python_altprovides,
  python_altprovides_once = python_altprovides_once,
}
