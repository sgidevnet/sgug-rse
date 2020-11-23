%global pypi_name u-msgpack-python

Name:           python-%{pypi_name}
Version:        2.5.0
Release:        3%{?dist}
Summary:        A portable, lightweight MessagePack serializer and deserializer

License:        MIT
URL:            https://github.com/vsergeev/u-msgpack-python
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%?python_enable_dependency_generator

%description
A lightweight MessagePack serializer and deserializer module written in pure
Python. It is fully compliant with the latest MessagePack specification.
In particular, it supports the new binary, UTF-8 string, and
application-defined ext types.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A lightweight MessagePack serializer and deserializer module written in pure
Python. It is fully compliant with the latest MessagePack specification.
In particular, it supports the new binary, UTF-8 string, and
application-defined ext types.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/umsgpack.py
%{python3_sitelib}/u_msgpack_python-%{version}-py?.?.egg-info


%changelog
* Mon Nov 23 2020  HAL <notes2@gmx.de> - 2.5.0-3
- compiles on Irix 6.5 with sgug-rse gcc 9.2. All tests pass.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Initial package
