%global luaver 5.3
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-alt-getopt
Version:        0.7.0
Release:        16%{?dist}
Summary:        Argument processing module for Lua

# license text requested from upstream:
# http://luaforge.net/tracker/index.php?func=detail&aid=47674
License:        MIT
URL:            http://sourceforge.net/projects/lua-alt-getopt/
Source0:        http://luaforge.net/frs/download.php/4260/lua-alt-getopt-0.7.0.tar.gz

BuildArch:      noarch
%if 0%{?fedora}
# not in RHEL / EPEL 6 yet
BuildRequires:  bmake
%endif
BuildRequires:  lua >= %{luaver}
Requires:       lua >= %{luaver}

%description
alt-getopt is a module for Lua programming language for processing
application's arguments the same way BSD/GNU getopt_long(3) functions
do. The main goal is compatibility with SUS "Utility Syntax
Guidelines" guidelines 3-13.


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
cp -p alt_getopt.lua $RPM_BUILD_ROOT%{luapkgdir}


%check
# This test routine assumes identical output,
# in identical order. This is a false assumption.
# At least in lua 5.2, the output is identical
# but the order is not (it seems to be random or 
# timing driven).
%if 0

%if 0%{?fedora}
bmake test
%else
echo 'running tests...'
ln -f -s `pwd`/alt_getopt.lua tests
export OBJDIR=`pwd`
if cd tests && ./test.sh;
then echo '   succeeded';
else echo '   failed'; false;
fi

%endif

%endif

%files
%doc ChangeLog NEWS README
%{luapkgdir}/alt_getopt.lua


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 0.7.0-8
- lua 5.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 0.7.0-5
- lua 5.2
- disabled tests

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Michel Salim <salimma@fedoraproject.org> - 0.7.0-1
- Initial package
