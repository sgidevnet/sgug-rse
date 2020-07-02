%global pypi_name u-msgpack-python

Name:           python-%{pypi_name}
Version:        2.6.0
Release:        1%{?dist}
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
* Tue May 26 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.2-1
- Update to 2.5.2 (#1697452)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Initial package
