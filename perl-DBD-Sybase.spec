%define upstream_name    DBD-Sybase
%define upstream_version 1.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.15
Release:	3

Summary:	Sybase database driver for the DBI module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~mewp/DBD-Sybase/
Source0:	http://www.cpan.org/authors/id/M/ME/MEWP/DBD-Sybase-1.15.tar.gz

BuildRequires:	freetds-devel
BuildRequires:	gettext-devel
BuildRequires:	perl-DBI >= 1.00
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
DBD::Sybase is a Perl module which works with the DBI module to provide access
to Sybase databases. With FreeTDS DBD::Sybase can be also used to query a
MS-SQL 7 or 2000 database server from a UNIX/Linux host.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export SYBASE=%{_prefix}
echo -e "\n\n\n\n\n\n" | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}" LD_RUN_PATH=""

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%{perl_vendorarch}/DBD/Sybase.pm
%{perl_vendorarch}/DBD/dbd-sybase.pod
%dir %{perl_vendorarch}/auto/DBD/Sybase
%attr(0755,root,root) %{perl_vendorarch}/auto/DBD/Sybase/Sybase.so
%{_mandir}/man3/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.120.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1
+ Revision: 659897
- update to new version 1.12
- update to new version 1.11

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 536457
- update to 1.10 (remove mdv patches)

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.0
+ Revision: 403094
- rebuild using %%perl_convert_version

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.09-1mdv2009.0
+ Revision: 289562
- fix deps
- try to fix build
- import perl-DBD-Sybase


* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.09-1mdv2009.0
- initial Mandriva package

