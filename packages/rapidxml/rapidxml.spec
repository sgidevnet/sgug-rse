Name:          rapidxml
Version:       1.13
Release:       12%{?dist}
Summary:       Fast XML parser
License:       Boost or MIT
URL:           http://rapidxml.sourceforge.net/
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}-with-tests.zip
Patch0:        %{name}-declarations.patch
BuildArch:     noarch
BuildRequires:  dos2unix

%description
RapidXml is an attempt to create the fastest XML parser possible, while
retaining usability, portability and reasonable W3C compatibility. It is an
in-situ parser written in modern C++, with parsing speed approaching that of
strlen function executed on the same data.

%package devel
Summary:       Fast XML parser
Provides:      %{name}-static = %{version}-%{release}

%description devel
RapidXml is an attempt to create the fastest XML parser possible, while
retaining usability, portability and reasonable W3C compatibility. It is an
in-situ parser written in modern C++, with parsing speed approaching that of
strlen function executed on the same data.

%prep
%setup -qn %{name}-%{version}-with-tests
%patch0 -p1

dos2unix license.txt

# Rename it to .h (but keep .hpp for tests)
sed -i 's/.hpp/.h/g' manual.html
for HPP in *.hpp; do
  cp -p $HPP ${HPP%hpp}h
  sed -i 's/.hpp/.h/g' ${HPP%hpp}h
done

%build
cd tests
# -jX is useless here
make build-g++-debug
cd -

%install
for H in *.h; do
  install -Dpm0644 $H %{buildroot}%{_includedir}/$H
done

%check
cd tests
# -jX is useless here
make run-g++-debug
cd -

%files devel
%doc license.txt manual.html
%{_includedir}/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 20 2013 Miro Hrončok <mhroncok@redhat.com> - 1.13-2
- devel subpackage now provides -static.

* Sat Feb 02 2013 Miro Hrončok <mhroncok@redhat.com> - 1.13-1
- Initial release
