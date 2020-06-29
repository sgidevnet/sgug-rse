%global _description %{expand:
Python interface to Bluetooth LE on Linux.
This is a project to provide an API to allow
access to Bluetooth Low Energy devices from Python.}

Name:           python-bluepy
Version:        1.3.0
Release:        3%{?dist}
Summary:        Python interface to Bluetooth LE

#bluepy uses code from the bluez project, which is made available under
#Version 2 of the GNU Public License, bluepy itself is placed in the
#public domain
License:        Public Domain and GPLv2
URL:            https://github.com/IanHarvey/bluepy
Source0:        https://github.com/IanHarvey/bluepy/archive/v/%{version}/bluepy-%{version}.tar.gz

%description %_description

%package -n python3-bluepy
Summary:        %{summary}
BuildRequires:  python3-devel make gcc
BuildRequires:  glib2-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
%{?python_provide:%python_provide python3-bluepy}

%description -n python3-bluepy %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n bluepy-v-%{version}
rm -rf bluepy.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%set_build_flags
export PYTHONPATH=../
sed 's|CFLAGS =|CFLAGS +=|g' -i bluepy/Makefile
sed 's|CPPFLAGS =|CPPFLAGS +=|g' -i bluepy/Makefile
sed 's| $(LDLIBS)| $(LDFLAGS) $(LDLIBS)|g' -i bluepy/Makefile
%py3_build
make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo,.nojekyll} -vf

%install
%py3_install
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitelib}/bluepy/{get_services,scanner}.py
for file in %{buildroot}%{_bindir}/{thingy52,sensortag,blescan}; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitelib}/bluepy/{get_services,scanner}.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitelib}/bluepy/{*.c,*.h}; do
   rm -rf $file
done

%files -n python3-bluepy
%{python3_sitelib}/bluepy/
%{python3_sitelib}/bluepy-*.egg-info/
%{_bindir}/blescan
%{_bindir}/sensortag
%{_bindir}/thingy52
%license LICENSE.txt
%doc README README.md

%files doc
%license LICENSE.txt
%doc docs/_build/html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 9 2019 Alessio <alciregi AT fedoraproject DOT org> - 1.3.0-1
- Initial package
