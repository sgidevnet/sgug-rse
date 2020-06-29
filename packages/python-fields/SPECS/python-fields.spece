%global srcname fields

Name:           python-%{srcname}
Version:        5.0.0
Release:        6%{?dist}
Summary:        Container class boilerplate killer

License:        BSD
URL:            https://github.com/ionelmc/%{name}
Source0:        https://github.com/ionelmc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Compatibility with python-sphinx >= 1.3, already applied upstream
Patch0:         %{name}-5.0.0-sphinx-1.3.patch

BuildArch:      noarch

%description
Container class boilerplate killer.

Features:
- Human-readable __repr__
- Complete set of comparison methods
- Keyword and positional argument support. Works like a normal class - you can
  override just about anything in the subclass (eg: a custom __init__). In
  contrast, hynek/characteristic forces different call schematics and calls
  your __init__ with different arguments.

%package doc
Summary:        Documentation for '%{name}'
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx-theme-py3doc-enhanced

%description doc
HTML API documentation for the '%{srcname}' Python module.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-benchmark

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     %{name}-doc = %{version}-%{release}
%endif # rhel

%description -n python%{python3_pkgversion}-%{srcname}
Container class boilerplate killer.

Features:
- Human-readable __repr__
- Complete set of comparison methods
- Keyword and positional argument support. Works like a normal class - you can
  override just about anything in the subclass (eg: a custom __init__). In
  contrast, hynek/characteristic forces different call schematics and calls
  your __init__ with different arguments.

%prep
%autosetup -p1
sed -i 's/\[pytest\]/\[tool:pytest\]/' setup.cfg

%build
%py3_build
PYTHONPATH=$PWD/src sphinx-build -b html docs docs/_build/html
rm -rf docs/_build/html/.buildinfo docs/_build/html/.doctrees

%install
%py3_install

%check
# Perf tests require unmaintained 'characteristic' module
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} \
  --ignore=tests/test_perf.py \
  tests

%files doc
%license LICENSE
%doc docs/_build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Scott K Logan <logans@cottsay.net> - 5.0.0-1
- Initial package
