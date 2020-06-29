%global pypi_name xmlschema
Name:           python-%{pypi_name}
Version:        1.0.18
Release:        3%{?dist}
Summary:        A Python XML Schema validator and decoder

License:        MIT
URL:            https://github.com/brunato/xmlschema
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
The xmlschema library is an implementation of XML Schema for Python.

This library arises from the needs of a solid Python layer for processing XML
Schema based files for MaX (Materials design at the Exascale) European project.
A significant problem is the encoding and the decoding of the XML data files
produced by different simulation software. Another important requirement is
the XML data validation, in order to put the produced data under control.
The lack of a suitable alternative for Python in the schema-based decoding
of XML data has led to build this library. Obviously this library can be
useful for other cases related to XML Schema based processing, not only for
the original scope.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}  %_description


%prep
%autosetup -n %{pypi_name}-%{version}
sed -i 's/~=/>=/' setup.py tox.ini  # https://bugzilla.redhat.com/show_bug.cgi?id=1758141
sed -i 's/==/>=/' tox.ini  # too strict test deps
pathfix.py -pni %{python3} %{pypi_name}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
# we exclude, not rm - used in %%check
%exclude %{python3_sitelib}/%{pypi_name}/tests


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.18-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.18-1
- Update to 1.0.18

* Tue Dec 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.16-1
- Initial package
