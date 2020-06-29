%global pypi_name elementpath
Name:           python-%{pypi_name}
Version:        1.4.0
Release:        4%{?dist}
Summary:        XPath 1.0/2.0 parsers and selectors for ElementTree and lxml

License:        MIT
URL:            https://github.com/sissaschool/elementpath
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros

# Circular test dependency on xmlschema and self
%bcond_without tests
%if %{with tests}
BuildRequires:  glibc-langpack-en
%endif

%global _description %{expand:
The proposal of this package is to provide XPath 1.0 and 2.0 selectors for
Python's ElementTree XML data structures, both for the standard ElementTree
library and for the lxml.etree library.

For lxml.etree this package can be useful for providing XPath 2.0 selectors,
because lxml.etree already has it's own implementation of XPath 1.0.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}  %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's/~=/>=/' setup.py tox.ini  # https://bugzilla.redhat.com/show_bug.cgi?id=1758141

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with tests}
%check
# The C.utf-8 locale fails with some straße related tests
# We could use a German locale, but English works fine
export LANG=en_US.utf-8
%tox
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.9

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Tue Dec 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-1
- Initial package
