%global pypi_name aenum

Name:           python-%{pypi_name}
Version:        2.2.3
Release:        3%{?dist}
Summary:        Advanced Enumerations, NamedTuples and NamedConstants for Python

License:        BSD
URL:            https://bitbucket.org/stoneleaf/aenum
Source0:        %{pypi_source}
BuildArch:      noarch

%description
aenum includes a Python stdlib Enum-compatible data type, as well as a
metaclass-based NamedTuple implementation and a NamedConstant class.

An Enum is a set of symbolic names (members) bound to unique, constant values.
Within an enumeration, the members can be compared by identity, and the
enumeration itself can be iterated over. Support exists for unique values,
multiple values, auto-numbering, and suspension of aliasing, plus the ability
to have values automatically bound to attributes.

A NamedTuple is a class-based, fixed-length tuple with a name for each
possible position accessible using attribute-access notation as well as
the standard index notation.

A NamedConstant is a class whose members cannot be rebound; it lacks all other
Enum capabilities, however.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aenum includes a Python stdlib Enum-compatible data type, as well as a
metaclass-based NamedTuple implementation and a NamedConstant class.

An Enum is a set of symbolic names (members) bound to unique, constant values.
Within an enumeration, the members can be compared by identity, and the
enumeration itself can be iterated over. Support exists for unique values,
multiple values, auto-numbering, and suspension of aliasing, plus the ability
to have values automatically bound to attributes.

A NamedTuple is a class-based, fixed-length tuple with a name for each
possible position accessible using attribute-access notation as well as
the standard index notation.

A NamedConstant is a class whose members cannot be rebound; it lacks all other
Enum capabilities, however.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} %{pypi_name}/test.py

%files -n python3-%{pypi_name}
%doc README aenum/doc aenum/CHANGES
%license aenum/LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.3-2
- Update to latest upstream release 2.2.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.4-1
- Switch to PyPI for the source to get rid of the BitBucket shortcomings
- Update to latest upstream release 2.1.4

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Update to latest upstream release 2.1.3
- Add license and docs (rhbz#1714003)

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Initial package for Fedora
