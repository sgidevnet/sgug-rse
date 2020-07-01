%global pypi_name pickleshare

Name:           python-%{pypi_name}
Version:        0.7.5
Release:        3%{?dist}
Summary:        Tiny 'shelve'-like database with concurrency support

License:        MIT
URL:            https://github.com/pickleshare/pickleshare
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
PickleShare - a small ‘shelve’ like data store with concurrency support.

Like shelve, a PickleShareDB object acts like a normal dictionary. 
Unlike shelve, many processes can access the database simultaneously. 
Changing a value in database is immediately visible to other processes 
accessing the same database.

Concurrency is possible because the values are stored in separate files. 
Hence the “database” is a directory where all files are governed 
by PickleShare.

%package -n     python3-%{pypi_name}
Summary:        Tiny 'shelve'-like database with concurrency support
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}

PickleShare - a small ‘shelve’ like data store with concurrency support.

Like shelve, a PickleShareDB object acts like a normal dictionary. 
Unlike shelve, many processes can access the database simultaneously. 
Changing a value in database is immediately visible to other processes 
accessing the same database.

Concurrency is possible because the values are stored in separate files. 
Hence the “database” is a directory where all files are governed 
by PickleShare.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# fix interpreter
sed -i 's/\/usr\/bin\/env python/\/usr\/bin\/python/' pickleshare.py

%build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%files -n python3-%{pypi_name} 
%license LICENSE

%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.5-1
- Update to 0.7.5

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-12
- Subpackage python2-pickleshare has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.4-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-4
- Rebuild for Python 3.6

* Wed Nov 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.4-3
- Do not own __pycache__ dir

* Sat Oct 01 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.4-2
- Fix typos and interpreter strings

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Fri Aug 12 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.7.3-1
- Initial package.
