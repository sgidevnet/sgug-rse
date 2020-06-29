%{?python_enable_dependency_generator}
%global srcname arpy

Name:          python-%{srcname}
Summary:       Library for accessing "ar" files
License:       BSD
URL:           https://pypi.org/project/arpy

Version:       1.1.1
Release:       8%{?dist}
Source0:       %{pypi_source}

BuildArch:     noarch

%description
arpy is a library for accessing the archive files and reading the contents.

It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-nose

%description -n python3-%{srcname}
arpy is a library for accessing the archive files and reading the contents.

It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

This package allows using arpy in Python 3 applications.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
nosetests-3

%files -n python3-%{srcname}
%{python3_sitelib}/arpy*
%{python3_sitelib}/__pycache__/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.1-2
- Enable python dependency generator

* Sat Aug 04 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.1.1-1
- Initial package for Fedora.
