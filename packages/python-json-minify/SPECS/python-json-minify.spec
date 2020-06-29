%global srcname json-minify
%global srcname_ json_minify
%global Srcname_ JSON_minify

Name:           python-%{srcname}
Version:        0.3.0
Release:        7%{?dist}
Summary:        Python port of the JSON-minify utility

License:        MIT
URL:            https://github.com/getify/JSON.minify/tree/python
Source0:        %pypi_source %{Srcname_}
BuildArch:      noarch

%description
JSON-minify minifies blocks of JSON-like content into valid JSON by removing
all whitespace *and* JS-style comments. With JSON-minify, you can maintain
developer-friendly JSON documents, but minify them before parsing or
transmitting them over-the-wire.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%{?python_enable_dependency_generator}

%description -n python3-%{srcname}
JSON-minify minifies blocks of JSON-like content into valid JSON by removing
all whitespace *and* JS-style comments. With JSON-minify, you can maintain
developer-friendly JSON documents, but minify them before parsing or
transmitting them over-the-wire.


%prep
%autosetup -n JSON_minify-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname_}
%{python3_sitelib}/%{Srcname_}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Initial package.
